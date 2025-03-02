import unittest
from leafnode import *

class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        n = LeafNode("p", "This is a paragraph of Test.")
        self.assertEqual(n.to_html(), "<p>This is a paragraph of Test.</p>")

    def test_to_html_with_props(self):
        n = LeafNode("a", "Click me!", {"href": "https://google.com"})
        self.assertEqual(n.to_html(), '<a href="https://google.com">Click me!</a>')

    def test_to_html_no_value(self):
        n = LeafNode("b", None)
        with self.assertRaises(ValueError):
            n.to_html()

    def test_to_html_no_tag(self):
        n = LeafNode(None, "I am the value")
        self.assertEqual(n.to_html(), "I am the value")
    
if __name__ == "__main__":
    unittest.main()
