import warnings
from typing import Mapping, Any
from textcompose.core import Component


def resolve_value(value, context: Mapping[str, Any], **kwargs) -> str | None:
    warnings.warn(
        "resolve_value is deprecated and will be removed in future versions. Use Component.resolve instead.",
        DeprecationWarning,
        stacklevel=2,
    )

    return Component.resolve(value, context, **kwargs)
