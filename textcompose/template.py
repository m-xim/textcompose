from typing import Any, Dict

from textcompose.container.container import BaseContainer
from textcompose.content.content import BaseContent, Condition


class Template(BaseContainer):
    def __init__(self, *components: BaseContent, when: Condition | None = None):
        super().__init__(when)
        self.components = components

    def render(self, context: Dict[str, Any], **kwargs) -> str:
        if not self._check_when(context, **kwargs):
            return ""

        parts = []
        for comp in self.components:
            if (part := self.resolve_value(comp, context, **kwargs)) is not None:
                parts.append(part)

        return "\n".join(parts).strip()
