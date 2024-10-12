import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", "italic")
        node2 = TextNode("This is a text node2", "bold")
        self.assertNotEqual(node, node2)

    def test_url_eq(self):
        node = TextNode(
            "This is a text node", "bold", "does it matter? if an url is a link"
        )
        node2 = TextNode(
            "This is a text node", "italic", "does it matter? if an url is a link"
        )
        self.assertEqual(node.url, node2.url)

    def test_url_not_eq(self):
        node = TextNode(
            "This is a text node", "bold", "does it matter? if an url is a link"
        )
        node2 = TextNode("This is a text node", "italic", "https://boot.dev")
        self.assertNotEqual(node.url, node2.url)

    def test_url_none(self):
        node = TextNode("This is a text node", "bold")
        self.assertIsNone(node.url)

    def test_texttype_eq(self):
        node = TextNode(
            "This is a text node with applepies",
            "italic",
            "does it matter? if an url is a link",
        )
        node2 = TextNode("This is a text node", "italic", "https://boot.dev")
        self.assertEqual(node.text_type, node2.text_type)


if __name__ == "__main__":
    unittest.main()
