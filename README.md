# try-slack-bolt

slack-bolt を利用した Slack アプリケーションです.

 * Slack Web API methods (https://api.slack.com/methods)
 * slack-bolt (https://github.com/slackapi/bolt-python)
 * Bolt 入門ガイド (https://slack.dev/bolt-python/ja-jp/tutorial/getting-started)

# セットアップ

(1) Slack アプリケーションを作成する.

以下を参考に Slack アプリケーションを作成します.

 * Bolt 入門ガイド (https://slack.dev/bolt-python/ja-jp/tutorial/getting-started)

作成したアプリケーションに対して以下の設定をおこないます.

 * "Basic Information" のページでアプリレベルトークンを生成し, 以下のスコープを許可します.
   - connections:write

 * "Socket Mode" のページでソケットモードを有効化します.

 * "Slash Commands" のページで以下のスラッシュコマンドを作成します.
   - /echo
   - /chat

 * "Event Subscriptions" のページで以下のイベントの受信を許可します.
   - message.channels
   - message.im
   - reaction_added

(2) 設定情報を作成する.

    config/export.sh.example を参考に config/export.sh を作成します.

(3) virtualenv をセットアップする.

    make setup

# 開発情報

    # アプリケーションを実行する.
    make run

    # テストを実行する.
    make test

    # テストのカバレッジを計測する.
    make coverage

    # 全ての make ゴールを表示する.
    make help

