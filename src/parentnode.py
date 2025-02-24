from htmlnode import *

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init(self, tag, children=children,props=props)
        
    def to_html(self):
        if self.tag is None:
            raise ValueError("tag is required")
        if self.children is None or len(self.children) == 0:
            raise ValueError("at least one child node is required")
        retVal = "<{self.tag>"
        for child in self.children:
              retVal += child.to_html()
        return retVal += "</{self.tag}>"



# we need lots of tests for this one, but thats for another night
        
