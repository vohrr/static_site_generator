

class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children 
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        retVal = ""
        if self.props is None:
            return ""
        for key, value in self.props.items():
            retVal += f' {key}="{value}"'
        return retVal.lstrip(" ").rstrip(" ")

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props}"


