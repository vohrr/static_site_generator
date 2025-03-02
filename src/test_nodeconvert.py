import unittest
from textnode import *
from nodeconvert import *



class TestNodeConvert(unittest.TestCase):
# text_node_to_html tests    
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

    def test_unsupported(self):
        n = TextNode("some text", None)
        with self.assertRaises(ValueError) as testcase:
            hn = text_node_to_html_node(n)
        self.assertEqual(str(testcase.exception), "Text type not supported")

# split_nodes_delimiter tests

    def test_basic(self):
        node = TextNode("This is text with a `code block` word", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(str(new_nodes),
                         '[TextNode(This is text with a , normal, None), TextNode(code block, code, None), TextNode( word, normal, None)]')

    def test_multiple(self):
        node = TextNode("`code block start` then normal *then bold* _then italic_ ", TextType.NORMAL)
        code_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        code_and_bold = split_nodes_delimiter(code_nodes, "*", TextType.BOLD)
        all_nodes = split_nodes_delimiter(code_and_bold, "_", TextType.ITALIC)
        self.assertEqual(str(all_nodes), "[TextNode(, normal, None), TextNode(code block start, code, None), TextNode( then normal , normal, None), TextNode(then bold, bold, None), TextNode( , normal, None), TextNode(then italic, italic, None), TextNode( , normal, None)]") 
                         
    def test_bad_syntax(self):
        node = TextNode("`code block start then normal *then bold* _then italic_ ", TextType.NORMAL)
        with self.assertRaises(ValueError) as testcase:
            new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(str(testcase.exception), "Invalid Markdown syntax")

    def test_empty_nodes(self):
        nodes = split_nodes_delimiter([], "*", TextType.BOLD)
        self.assertEqual(nodes, [])


        
        
        
        
        
