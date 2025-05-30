from typing import Dict, Any, Optional
from textcompose.content.content import BaseContent, Condition, Value


class I18nTC(BaseContent):
    def __init__(
        self,
        text: str,
        when: Optional[Condition] = None,
        locale: Optional[Value] = None,
        /,
        **mapping: Value,
    ) -> None:
        super().__init__(when=when)
        self.text = text
        self.locale = locale
        self.mapping = mapping

    def _resolve_mapping(self, context: Dict[str, Any]) -> Dict[str, Any]:
        resolved = {}
        for key, val in self.mapping.items():
            result = self.resolve_value(val, context)
            resolved[key] = result if result is not None else ""
        return resolved

    def render(self, context: Dict[str, Any], **kwargs) -> Optional[str]:
        if not self._check_when(context, **kwargs):
            return None

        i18n = kwargs.get("i18n")
        if i18n is None:
            raise ValueError("Missing 'i18n' in render kwargs")

        params = self._resolve_mapping(context)
        locale = self.resolve_value(self.locale, context) if self.locale else None

        return i18n.get(self.text, locale, **params)
