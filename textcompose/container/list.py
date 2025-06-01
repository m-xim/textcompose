from typing import Union, Callable, Any, Iterable, Optional, Mapping

from magic_filter import MagicFilter

from textcompose.container.base import Container
from textcompose.core import Value, Condition, resolve_value


class List(Container):
    def __init__(
        self,
        *items: Value,
        getter: Union[MagicFilter, Callable[[Mapping[str, Any]], Iterable]],
        sep: Optional[str] = "\n\n",
        inner_sep: str = "\n",
        when: Condition | None = None,
    ) -> None:
        super().__init__(*items, when=when)
        self.items = items
        self.getter = getter
        self.sep = sep
        self.inner_sep = inner_sep

    def _render_item(self, item_value: Any, context: Mapping[str, Any], **kwargs) -> str | None:
        rendered_parts = [
            resolve_value(item_tpl, {"item": item_value, "context": context}, **kwargs) for item_tpl in self.items
        ]
        return self.inner_sep.join(filter(None, rendered_parts)) or None

    def render(self, context, **kwargs) -> str | None:
        if not self._check_when(context, **kwargs):
            return None

        items_iterable = resolve_value(self.getter, context, **kwargs)
        if not items_iterable:
            return None

        rendered_items = [self._render_item(item_value, context, **kwargs) for item_value in items_iterable]

        return self.sep.join(filter(None, rendered_items)) or None
