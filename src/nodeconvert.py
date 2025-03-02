from textnode import *
from leafnode import *
import re

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


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    if len(old_nodes) == 0: 
        return old_nodes
    for node in old_nodes:
        if node.text_type is not TextType.NORMAL:
            new_nodes.append(node)
        else:
            split_nodes = node.text.split(delimiter)
            if len(split_nodes) % 2 == 0:
                raise ValueError("Invalid Markdown syntax")
            for index, value in enumerate(split_nodes):
                if index % 2 == 0:
                    new_nodes.append(TextNode(value, TextType.NORMAL))
                else:
                    new_nodes.append(TextNode(value, text_type))
    return new_nodes

def extract_markdown_images(text):
    #takes raw markdown text and returns a list of tuples
    #remember that markdown for images follows the pattern:
    # ![displaytext](url) 
    # re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text) 





