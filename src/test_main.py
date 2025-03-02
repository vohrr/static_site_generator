import unittest
from textnode import *
from main import *

class TestMain(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.NORMAL)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This test should be bold!", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'b')
        self.assertEqual(html_node.value, 'This test should be bold!')

    def test_italic(self):
        node = TextNode("These letters are italic", TextType.ITALIC)
        hn = text_node_to_html_node(node)
        self.assertEqual(hn.tag, 'i')
        self.assertEqual(hn.value, node.text)

    def test_code(self):
        n = TextNode("code tag", TextType.CODE)
        hn = text_node_to_html_node(n)
        self.assertEqual(hn.tag, 'code')
        self.assertEqual(hn.value, n.text)
        self.assertEqual(hn.props, None)

    def test_links(self):
        n = TextNode("should be an href", TextType.LINK, "google.com")
        hn = text_node_to_html_node(n)
        self.assertEqual(hn.tag, 'a')
        self.assertEqual(hn.props, { 'href' : 'google.com' })
        self.assertEqual(hn.value, n.text)

    def test_image(self):
        n = TextNode("picture time", TextType.IMAGE, 'imgur.com/picture')
        hn = text_node_to_html_node(n)
        self.assertEqual(hn.tag, 'img')
        self.assertEqual(hn.value, '')
        self.assertEqual(hn.props, { 'src' : 'imgur.com/picture'})






        
        
        
        
        
