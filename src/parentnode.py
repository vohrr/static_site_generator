from htmlnode import *

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, children=children,props=props)
        
    def to_html(self):
        if self.tag is None:
            raise ValueError("Tag is required")
        if self.children is None or len(self.children) == 0:
            raise ValueError("At least one child node is required")
        retVal = f"<{self.tag}>"
        for child in self.children:
            retVal += child.to_html()
        return retVal + f"</{self.tag}>"



        
