from textcompose.containers.base import Container
from textcompose.core import Value, Condition


class Group(Container):
    def __init__(self, *items: Value, sep: Value = "\n", when: Condition | None = None) -> None:
        super().__init__(*items, when=when)
        self.sep = sep

    def render(self, context, **kwargs) -> str | None:
        if not self._check_when(context, **kwargs):
            return None

        parts = []
        for comp in self.items:
            if (part := self.resolve(comp, context, **kwargs)) is not None:
                parts.append(part)

        sep = self.resolve(self.sep, context, **kwargs)
        return sep.join(parts) if parts else None
