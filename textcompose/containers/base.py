from abc import ABC, abstractmethod

from textcompose.core import Component, Value, Condition


class Container(Component, ABC):
    @abstractmethod
    def __init__(self, *items: Value, when: Condition | None = None) -> None:
        super().__init__(when=when)
        self.items = items
