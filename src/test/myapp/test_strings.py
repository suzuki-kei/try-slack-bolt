from myapp.strings import *
from parameterized import parameterized
import unittest


class StripHeredocTestCase(unittest.TestCase):

    @parameterized.expand([
        ("", ""),
        ("a", " a"),
        ("a \nb \nc", " a \n b \n c \n"),
        (
            "\n".join([
                "aaa",
                "bbb",
                "ccc",
            ]),
            """
                aaa
                bbb
                ccc
            """
        ),
        (
            "\n".join([
                "NAME",
                "    command-name",
                "",
                "EXIT STATUS",
                "    0 if successfully.",
                "    1 if invalid argument passed.",
            ]),
            """
                NAME
                    command-name

                EXIT STATUS
                    0 if successfully.
                    1 if invalid argument passed.
            """
        ),
    ])
    def test_strip_heredoc(self, expected, text):
        actual = strip_heredoc(text)
        self.assertEqual(expected, actual)

