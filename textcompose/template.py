from typing import Optional

from textcompose.containers.base import Container
from textcompose.core import Component, Condition, resolve_value


class Template(Container):
    def __init__(self, *items: Component, sep: Optional[str] = "\n", when: Condition | None = None):
        super().__init__(when=when)
        self.items = items
        self.sep = sep

    def render(self, context, **kwargs) -> str:
        if not self._check_when(context, **kwargs):
            return ""

        parts = []
        for comp in self.items:
            if (part := resolve_value(comp, context, **kwargs)) is not None:
                parts.append(part)

        return self.sep.join(parts).strip()
