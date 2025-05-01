from magic_filter import MagicFilter
from abc import ABC, abstractmethod
from typing import Any, Callable

Condition = bool | Callable[[dict[str, Any]], bool] | "BaseContent"


class BaseContent(ABC):
    def __init__(self, when: Condition | None = None) -> None:
        self.when = when

    def _check_when(self, context: dict[str, Any]) -> bool:
        if self.when is None:
            return True
        if isinstance(self.when, MagicFilter):
            return bool(self.when.resolve(context))
        if isinstance(self.when, BaseContent):
            text = self.when.render(context)
            return bool(text.strip())
        if callable(self.when):
            return bool(self.when(context))
        return bool(self.when)

    @abstractmethod
    def render(self, context: dict[str, Any]) -> str | None: ...
