from magic_filter import MagicFilter
from abc import ABC, abstractmethod
from typing import Any, Callable, Union

from textcompose.utils.resolve_value import resolve_value

Value = Union[None, MagicFilter, str, "BaseContent"]
Condition = Union[None, MagicFilter, Callable[[dict[str, Any]], bool], bool, "BaseContent"]


class BaseContent(ABC):
    def __init__(self, when: Condition | None = None) -> None:
        self.when = when

    def _check_when(self, context: dict[str, Any], **kwargs) -> bool:
        if self.when is None:
            return True

        resolved = resolve_value(value=self.when, context=context, **kwargs)
        resolved = resolved.strip() if isinstance(resolved, str) else resolved
        return bool(resolved)

    @abstractmethod
    def render(self, context: dict[str, Any], **kwargs) -> str | None: ...
