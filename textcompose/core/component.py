from abc import ABC, abstractmethod
from typing import Any, Mapping, Callable

from box import Box
from magic_filter import MagicFilter

# Direct import to prevent circular import issues
from textcompose.core.types import Condition


class Component(ABC):
    def __init__(self, when: Condition | None = None) -> None:
        self.when = when

    @staticmethod
    def resolve(value, context: Mapping[str, Any], **kwargs) -> str | None:
        context = Box(context)
        if isinstance(value, MagicFilter):
            return value.resolve(context)
        elif hasattr(value, "render") and callable(getattr(value, "render")):
            return value.render(context, **kwargs)
        elif isinstance(value, Callable):
            return value(context)
        return value

    def _check_when(self, context: Mapping[str, Any], **kwargs) -> bool:
        if self.when is None:
            return True

        # If self.when is a string, treat it as a variable name in the context and return its boolean value.
        if isinstance(self.when, str):
            return bool(context.get(self.when))

        return bool(self.resolve(value=self.when, context=context, **kwargs))

    @abstractmethod
    def render(self, context: Mapping[str, Any], **kwargs) -> str | None: ...
