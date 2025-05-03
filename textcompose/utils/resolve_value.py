from magic_filter import MagicFilter
from textcompose.content.content import BaseContent, Value


def resolve_value(value: Value, context: dict, **kwargs) -> str | None:
    if isinstance(value, BaseContent):
        return value.render(context, **kwargs)
    elif isinstance(value, MagicFilter):
        return value.resolve(context)
    return value
