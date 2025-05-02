from abc import abstractmethod
from typing import Any

from textcompose.content.content import BaseContent, Condition


class BaseContainer(BaseContent):
    def __init__(self, *children: BaseContent, when: Condition | None = None) -> None:
        super().__init__(when=when)
        self.children = children

    @abstractmethod
    def render(self, context: dict[str, Any], **kwargs) -> str | None: ...
