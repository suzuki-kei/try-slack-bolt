import os


class LoadSettingsError(Exception):
    """
        設定情報の読み込みに失敗したことを表す例外.
    """


class Settings(object):

    __slots__ = (
        "SLACK_APP_TOKEN",
        "SLACK_BOT_TOKEN",
        "SLACK_BOT_USER_ID",
        "SLACK_REACTION_TO_DELETE_MESSAGE",
    )

    def __init__(self):
        try:
            self.SLACK_APP_TOKEN = _get_string("SLACK_APP_TOKEN")
            self.SLACK_BOT_TOKEN = _get_string("SLACK_BOT_TOKEN")
            self.SLACK_BOT_USER_ID = _get_string("SLACK_BOT_USER_ID")
            self.SLACK_REACTION_TO_DELETE_MESSAGE = _get_string("SLACK_REACTION_TO_DELETE_MESSAGE")
        except KeyError:
            raise LoadSettingsError()


def _get_string(key: str) -> str:
    value = os.environ.get(key)
    if value is None or value.strip() == "":
        raise LoadSettingsError(f"{key}=[{value}]")
    return value.strip()

