from typing import Union, Callable, Any, TYPE_CHECKING, Mapping

from magic_filter import MagicFilter

if TYPE_CHECKING:
    from textcompose.core.component import Component  # type: ignore[unused-import]

Value = Union[MagicFilter, str, Callable[[Mapping[str, Any]], str | None], "Component"]
Condition = Union[MagicFilter, Callable[[Mapping[str, Any]], bool], bool, "Component"]
