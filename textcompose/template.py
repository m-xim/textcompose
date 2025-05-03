from typing import Any, Dict

from textcompose.container.container import BaseContainer
from textcompose.content.content import BaseContent, Condition
from textcompose.utils.resolve_value import resolve_value


class Template(BaseContainer):
    def __init__(self, *components: BaseContent, when: Condition | None = None):
        super().__init__(when)
        self.components = components

    def render(self, context: Dict[str, Any], **kwargs) -> str:
        if not self._check_when(context, **kwargs):
            return ""

        parts = []
        for comp in self.components:
            if (part := resolve_value(comp, context, **kwargs)) is not None:
                parts.append(part)

        return "\n".join(parts).strip()
