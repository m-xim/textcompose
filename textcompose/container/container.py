from abc import abstractmethod
from typing import Any

from textcompose.content.content import BaseContent, Condition


class BaseContainer(BaseContent):
    def __init__(self, children: list[BaseContent], when: Condition | None = None) -> None:
        super().__init__(when)
        self.children = children

    @abstractmethod
    def render(self, context: dict[str, Any]) -> str | None: ...
