from typing import Union, Callable, Any, Iterable, Mapping

from magic_filter import MagicFilter

from textcompose.containers.base import Container
from textcompose.core import Value, Condition


class List(Container):
    def __init__(
        self,
        *items: Value,
        getter: Union[MagicFilter, Callable[[Mapping[str, Any]], Iterable]],
        sep: Value = "\n\n",
        inner_sep: Value = "\n",
        when: Condition | None = None,
    ) -> None:
        super().__init__(*items, when=when)
        self.items = items
        self.getter = getter
        self.sep = sep
        self.inner_sep = inner_sep

    def _render_item(self, context: Mapping[str, Any], inner_sep: str, **kwargs) -> str | None:
        rendered_parts = [self.resolve(item_tpl, context, **kwargs) for i, item_tpl in enumerate(self.items)]
        return inner_sep.join(filter(None, rendered_parts)) or None

    def render(self, context, **kwargs) -> str | None:
        if not self._check_when(context, **kwargs):
            return None

        items_iterable = self.resolve(self.getter, context, **kwargs)
        if not items_iterable:
            return None

        inner_sep = self.resolve(self.inner_sep, context, **kwargs)

        rendered_items = [
            self._render_item(
                context={"item": item_value, "context": getattr(context, "context", context), "i": i},
                inner_sep=inner_sep,
                **kwargs,
            )
            for i, item_value in enumerate(items_iterable)
        ]

        sep = self.resolve(self.sep, context, **kwargs)
        return sep.join(filter(None, rendered_items)) or None
