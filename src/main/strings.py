import textwrap


def strip_heredoc(text: str) -> str:
    """
    """
    return textwrap.dedent(text).strip()

