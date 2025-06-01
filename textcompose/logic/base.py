from abc import ABC, abstractmethod

from textcompose.core import Component, Condition


class Logic(Component, ABC):
    @abstractmethod
    def __init__(self, when: Condition | None = None, *args, **kwargs):
        super().__init__(when=when)
