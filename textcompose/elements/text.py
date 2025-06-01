from textcompose.core import Condition
from textcompose.elements.base import Element


class Text(Element):
    def __init__(self, text: str, when: Condition | None = None):
        super().__init__(when=when)
        self.text = text

    def render(self, context, **kwargs) -> str | None:
        if not self._check_when(context, **kwargs):
            return None
        return self.text
