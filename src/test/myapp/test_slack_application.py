from myapp.slack_application import *
from parameterized import parameterized
import unittest


class RemoveFirstMentionStringTestCase(unittest.TestCase):

    @parameterized.expand([
        ("", ""),
        ("a", "a"),
        ("", "<@ABCDEFG>"),
        (" aaa", "<@ABCDEFG> aaa"),
        ("aaa  bbb", "aaa <@ABCDEFG> bbb"),
        ("aaa  bbb <@ABCDEFG> ccc", "aaa <@ABCDEFG> bbb <@ABCDEFG> ccc"),
    ])
    def test_remove_first_mention_string(self, expected, text):
        actual = remove_first_mention_string(text)
        self.assertEqual(expected, actual)

