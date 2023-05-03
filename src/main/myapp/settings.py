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
            self.SLACK_APP_TOKEN = os.environ["SLACK_APP_TOKEN"]
            self.SLACK_BOT_TOKEN = os.environ["SLACK_BOT_TOKEN"]
            self.SLACK_BOT_USER_ID = "U055Z4SJR5Z"
            self.SLACK_REACTION_TO_DELETE_MESSAGE = "white_check_mark"
        except KeyError:
            raise LoadSettingsError()

