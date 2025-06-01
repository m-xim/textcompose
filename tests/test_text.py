import pytest
from magic_filter import F

from textcompose.elements import Text


@pytest.mark.parametrize(
    "text,when,context,expected",
    [
        ("hello", None, None, "hello"),
        ("world", True, {}, "world"),
        ("skip", False, {}, None),
        ("func", lambda ctx: ctx["ok"], {"ok": True}, "func"),
        ("func", lambda ctx: ctx["ok"], {"ok": False}, None),
        ("mf", F["ok"], {"ok": True}, "mf"),
        ("mf", F["ok"], {"ok": False}, None),
        ("bc", Text("bc"), {}, "bc"),
        ("none", None, {}, "none"),
        ("empty", True, {}, "empty"),
        ("empty_str", True, {}, "empty_str"),
        ("zero", True, {}, "zero"),
        ("none_when", None, {}, "none_when"),
    ],
    ids=[
        "plain-none",
        "plain-true",
        "plain-false",
        "lambda-true",
        "lambda-false",
        "magicfilter-true",
        "magicfilter-false",
        "nested-text",
        "none-text",
        "empty-text",
        "empty-str",
        "zero-text",
        "none-when",
    ],
)
def test_text_types(text, when, context, expected):
    result = Text(text, when=when).render(context)
    assert result == expected
