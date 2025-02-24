from htmlnode import *

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, props=props)
    
    def __repr__(self):
        print(f"{self}")

    def to_html(self):
        if self.value is None:
            raise ValueError("Value is required")
        if self.tag is None:
            return self.value
        if self.props is None:
            return f"<{self.tag}>{self.value}</{self.tag}>"
                
        return f"<{self.tag} {super().props_to_html()}>{self.value}</{self.tag}>"
        
