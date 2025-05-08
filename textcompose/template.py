from typing import Any, Dict, Optional

from textcompose.container.container import BaseContainer
from textcompose.content.content import BaseContent, Condition


class Template(BaseContainer):
    def __init__(self, *components: BaseContent, sep: Optional[str] = "\n", when: Condition | None = None):
        super().__init__(when)
        self.components = components
        self.sep = sep

    def render(self, context: Dict[str, Any], **kwargs) -> str:
        if not self._check_when(context, **kwargs):
            return ""

        parts = []
        for comp in self.components:
            if (part := self.resolve_value(comp, context, **kwargs)) is not None:
                parts.append(part)

        return self.sep.join(parts).strip()
