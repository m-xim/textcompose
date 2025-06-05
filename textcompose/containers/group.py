from typing import Optional

from textcompose.containers.base import Container
from textcompose.core import Value, Condition, resolve_value


class Group(Container):
    def __init__(self, *items: Value, sep: Optional[str] = "\n", when: Condition | None = None) -> None:
        super().__init__(*items, when=when)
        self.sep = sep

    def render(self, context, **kwargs) -> str | None:
        if not self._check_when(context, **kwargs):
            return None

        parts = []
        for comp in self.items:
            if (part := resolve_value(comp, context, **kwargs)) is not None:
                parts.append(part)
        return self.sep.join(parts) if parts else None
