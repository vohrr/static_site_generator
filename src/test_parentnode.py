from parentnode import *
from leafnode import *
import unittest

class TestParentNode(unittest.TestCase):
    def test_no_tag_raise_error(self):
        pn = ParentNode(None, [LeafNode(None, "Im a leaf", None)])
        with self.assertRaises(ValueError) as testcase:
            pn.to_html()
        self.assertEqual(str(testcase.exception), "Tag is required")

    def test_no_children_raise_error(self):
        pn = ParentNode("<a>", None)
        with self.assertRaises(ValueError) as testcase:
            pn.to_html()
        self.assertEqual(str(testcase.exception), "At least one child node is required")

    def test_many_children(self):
        pn = ParentNode(
                "p", 
                [
                    LeafNode("b", "Bold text"),
                    LeafNode(None, "NorMalTexT"),
                    LeafNode("i", "italic text"),
                    LeafNode(None, "nORmAL tEXt"),
                ],
        )
        result = pn.to_html()
        self.assertEqual("<p><b>Bold text</b>NorMalTexT<i>italic text</i>nORmAL tEXt</p>", result)

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")
    
    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_nested_parents(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node, grandchild_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span><b>grandchild</b></div>",
        )
# need test to validate several different variations of child nodes
