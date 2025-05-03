from abc import ABC, abstractmethod
from typing import Any, Callable, Union

from magic_filter import MagicFilter

Value = Union[None, MagicFilter, str, "BaseContent"]
Condition = Union[None, MagicFilter, Callable[[dict[str, Any]], bool], bool, "BaseContent"]


class BaseContent(ABC):
    def __init__(self, when: Condition | None = None) -> None:
        self.when = when

    @staticmethod
    def resolve_value(value: Value, context: dict, **kwargs) -> str | None:
        if isinstance(value, BaseContent):
            return value.render(context, **kwargs)
        elif isinstance(value, MagicFilter):
            return value.resolve(context)
        elif isinstance(value, Callable):
            return value(context)
        return value

    def _check_when(self, context: dict[str, Any], **kwargs) -> bool:
        if self.when is None:
            return True

        resolved = self.resolve_value(value=self.when, context=context, **kwargs)
        print(resolved)
        resolved = resolved.strip() if isinstance(resolved, str) else resolved
        return bool(resolved)

    @abstractmethod
    def render(self, context: dict[str, Any], **kwargs) -> str | None: ...
