import textwrap


def strip_heredoc(text: str) -> str:
    """
        各行の共通するインデントを削除し, 文字列全体を str.strip() する.

        Arguments
        ---------
        text: str
            処理対象のテキスト.

        Returns
        -------
        str
            処理後のテキスト.
    """
    return textwrap.dedent(text).strip()

