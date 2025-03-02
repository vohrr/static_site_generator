from textnode import *
from leafnode import *

def main():
    node = TextNode("This is a text node", TextType.NORMAL)
#    html_node = text_node_to_html_node(node)
    print(node)
#    print(html_node)

def text_node_to_html_node(text_node):
    if text_node.text_type not in TextType:
        raise ValueError("Text type not supported")
    if text_node.text_type == TextType.NORMAL:
        return LeafNode(None, text_node.text)
    elif text_node.text_type == TextType.BOLD:
        return LeafNode('b', text_node.text)
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode('i', text_node.text)
    elif text_node.text_type == TextType.CODE:
        return LeafNode('code', text_node.text)
    elif text_node.text_type == TextType.LINK:
        return LeafNode('a', text_node.text, { 'href': text_node.url } )
    elif text_node.text_type == TextType.IMAGE:
        return LeafNode('img', '', {'src' : text_node.url })
    else:
        raise ValueError("Conversion from text not found")


def markdown_to_text_node(text):
    pass

main()
