from typing import Dict, Any
from textcompose.content.content import BaseContent, Condition


class Text(BaseContent):
    def __init__(self, text: str, when: Condition | None = None):
        super().__init__(when)
        self.text = text

    def render(self, context: Dict[str, Any]) -> str | None:
        if not self._check_when(context):
            return None
        return self.text
