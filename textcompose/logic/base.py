from textcompose.content.content import BaseContent, Condition, Value
from typing import Any, Optional, Dict


class If(BaseContent):
    def __init__(
        self,
        if_: Condition,
        then_: Optional[Value] = None,
        else_: Optional[Value] = None,
        when: Condition | None = None,
    ):
        super().__init__(when)
        self.if_ = if_
        self.then_ = then_
        self.else_ = else_

    def render(self, context: Dict[str, Any], **kwargs) -> Optional[str]:
        if not self._check_when(context, **kwargs):
            return None

        if bool(self.resolve_value(value=self.if_, context=context, **kwargs)):
            return self.resolve_value(self.then_, context, **kwargs)
        return self.resolve_value(self.else_, context, **kwargs)
