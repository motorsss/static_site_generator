import unittest
from htmlnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_props(self):
        node = LeafNode(
            "h1",
            "test value",
            {"class": "nuts", "href": "https://deez.pistachios"}
        )
        self.assertEqual(node.props_to_html(),
                         ' class="nuts" href="https://deez.pistachios"')

    def test_attr(self):
        node = LeafNode("p", "test paragraph")
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "test paragraph")
        self.assertEqual(node.props, None)

    def test_repr(self):
        node = LeafNode('div', 'what is div?', {'src': 'ligma.jpg'})

        self.assertEqual(node.__repr__(),
                         "LeafNode(div, what is div?, {'src': 'ligma.jpg'})"
                         )


if __name__ == "__main__":
    unittest.main()
