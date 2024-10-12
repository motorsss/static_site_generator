import unittest
from htmlnode import *


class TestHTMLNode(unittest.TestCase):
    def test_props(self):
        node = HTMLNode(
            "h1",
            "test value",
            None,
            {"class": "nuts", "href": "https://deez.pistachios"}
        )
        self.assertEqual(node.props_to_html(),' class="nuts" href="https://deez.pistachios"')

    def test_attr(self):
        node = HTMLNode("p", "test paragrapgh")
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "test paragrapgh")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

    def test_repr(self):
        node = HTMLNode('div', 'what is div?', None, {'src': 'ligma.jpg'})

        self.assertEqual(node.__repr__(),
                         "HTMLNode(div, what is div?, children: None, {'src': 'ligma.jpg'})"
                         )