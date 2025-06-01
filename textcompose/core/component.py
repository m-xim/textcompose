from abc import ABC, abstractmethod
from typing import Any, Mapping

# Direct import to prevent circular import issues
from textcompose.core.resolvers import resolve_value
from textcompose.core.types import Condition


class Component(ABC):
    def __init__(self, when: Condition | None = None) -> None:
        self.when = when

    def _check_when(self, context: Mapping[str, Any], **kwargs) -> bool:
        if self.when is None:
            return True

        resolved = resolve_value(value=self.when, context=context, **kwargs)
        resolved = resolved.strip() if isinstance(resolved, str) else resolved
        return bool(resolved)

    @abstractmethod
    def render(self, context: Mapping[str, Any], **kwargs) -> str | None: ...
