from textcompose.core import Condition
from textcompose.elements.base import Element


class Format(Element):
    def __init__(self, template: str, when: Condition | None = None) -> None:
        super().__init__(when=when)
        self.template = template

    def render(self, context, **kwargs) -> str | None:
        if not self._check_when(context, **kwargs):
            return None
        return self.template.format_map(context)
