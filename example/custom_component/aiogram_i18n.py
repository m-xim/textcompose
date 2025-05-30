from typing import Dict, Any
from textcompose.content.content import BaseContent, Condition


class I18nTC(BaseContent):
    def __init__(self, key: str, when: Condition | None = None):
        super().__init__(when=when)
        self.key = key

    def render(self, context: Dict[str, Any], **kwargs) -> str | None:
        if not self._check_when(context):
            return None

        i18n = kwargs.get("i18n")
        if i18n is None:
            raise RuntimeError("aiogram_i18n not configured")
        return i18n.get(self.key)
