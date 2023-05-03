from settings import Settings
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from strings import strip_heredoc
import re


def create_socket_mode_handler(settings: Settings) -> SocketModeHandler:
    app = App(token=settings.SLACK_BOT_TOKEN)
    prepare_handlers(app, settings)
    return SocketModeHandler(app, settings.SLACK_APP_TOKEN)


def prepare_handlers(app: App, settings: Settings) -> None:

    @app.command("/echo")
    def handle_command_echo(ack, respond, command):
        text = command["text"]
        ack()
        respond(text)

    @app.command("/chat")
    def handle_command_chat(ack, respond, command):
        text = command["text"]
        ack()

        if text == "help":
            respond(strip_heredoc("""
                * 公開チャネルでメンションするとボットが返信します。
                * DM を送るとボットが返信します（メンションは不要です）。
                * ボットの投稿に :white_check_mark: でリアクションすると投稿を削除します。
                * スラッシュメッセージ "/echo [message]" で指定したメッセージをそのまま表示します。
                * スラッシュメッセージ "/chat help" でボットの使い方を表示します。
            """))
            return

        respond(strip_heredoc(f"""
            無効なコマンドです: {text}
            /chat help で使い方を表示できます。
        """))

    #
    # [NOTE]
    # app_mention に対するハンドラは定義しない.
    # メンションされた場合に app_mention と message の両方が呼び出されるため.
    #
    #     @app.event("app_mention")
    #     def handle_event_app_mention(...):
    #         ...
    #

    @app.event("reaction_added")
    def handle_event_reaction_added(event, client):
        ts = event["item"]["ts"]
        channel = event["item"]["channel"]
        reaction = event["reaction"]
        item_user = event.get("item_user")

        if reaction != settings.SLACK_REACTION_TO_DELETE_MESSAGE:
            return
        if item_user != settings.SLACK_BOT_USER_ID:
            return
        client.chat_delete(ts=ts, channel=channel)

    @app.event("message")
    def handle_event_message(event, client):
        text = event.get("text", "")
        has_mention = text.find(f"<@{settings.SLACK_BOT_USER_ID}>") != -1
        is_reply_message = "thread_ts" in event
        is_direct_message = event.get("channel_type") == "im"
        is_message_posted = "subtype" not in event

        if not is_message_posted:
            return
        if not (has_mention or is_direct_message or is_reply_message):
            return

        ts = event["ts"]
        channel = event["channel"]
        client.chat_postMessage(channel=channel, thread_ts=ts, text="hello")


def remove_first_mention_string(text: str) -> str:
    """
        最初のメンション文字列を削除する.
    """
    return re.compile(r"<@.+?>").sub("", text, 1).strip()

