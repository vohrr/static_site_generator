import unittest
from htmlnode import *

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        n1 = HTMLNode("input", "", props = { "type" : "text" })
        self.assertEqual('type="text"', n1.props_to_html()) 

    def test_props_to_html_2(self):
        n1 = HTMLNode("p", "This is a paragraph", props = { "href" : "https//www.google.com", "target" : "_blank" })
        self.assertEqual('href="https//www.google.com" target="_blank"', n1.props_to_html())

    def test_props_to_html_3(self):
        n1 = HTMLNode("div", "Some text inside a div", props = { "style" : "width:200", "class": "center" })
        self.assertEqual('style="width:200" class="center"', n1.props_to_html())

    def test_empty_props(self):
        n1 = HTMLNode()
        self.assertEqual("", n1.props_to_html())

if __name__ == "__main__":
    unittest.main()
