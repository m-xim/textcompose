from typing import Callable, Mapping, Any

from magic_filter import MagicFilter


def resolve_value(value, context: Mapping[str, Any], **kwargs) -> str | None:
    if isinstance(value, MagicFilter):
        return value.resolve(context)
    elif hasattr(value, "render") and callable(getattr(value, "render")):
        return value.render(context, **kwargs)
    elif isinstance(value, Callable):
        return value(context)
    return value
