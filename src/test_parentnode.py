import unittest
from htmlnode import *


class TestParentNode(unittest.TestCase):
    def test_parent_tohtml(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold Text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold Text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_parent_tohtml2(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold Text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
            {"href": "default.asp"},
        )
        self.assertEqual(
            node.to_html(),
            '<p href="default.asp"><b>Bold Text</b>Normal text<i>italic text</i>Normal text</p>',
        )

    def test_grandparent(self):
        grandchild = LeafNode("p", "this is a paragraph")
        parent = ParentNode("h1", [grandchild])
        granddaddy = ParentNode("body", [parent])
        self.assertEqual(granddaddy.to_html(),
                         "<body><h1><p>this is a paragraph</p></h1></body>"
                         )


if __name__ == "__main__":
    unittest.main()
