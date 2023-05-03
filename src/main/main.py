from settings import Settings
from slack_application import create_socket_mode_handler


def main():
    try:
        settings = Settings()
        handler = create_socket_mode_handler(settings)
        handler.start()
    except KeyboardInterrupt:
        pass # Ctrl+C が押された場合は終了する.


if __name__ == "__main__":
    main()

