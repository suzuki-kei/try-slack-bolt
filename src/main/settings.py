import os


class LoadSettingsError(Exception):
    """
        設定情報の読み込みに失敗したことを表す例外.
    """


class Settings(object):

    slots = (
        "SLACK_APP_TOKEN",
        "SLACK_BOT_TOKEN",
    )

    def __init__(self):
        try:
            self.SLACK_APP_TOKEN = os.environ["SLACK_APP_TOKEN"]
            self.SLACK_BOT_TOKEN = os.environ["SLACK_BOT_TOKEN"]
        except KeyError:
            raise LoadSettingsError()

