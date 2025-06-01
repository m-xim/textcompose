import pytest

from textcompose.elements.format import Format


@pytest.mark.parametrize(
    "template,context,when,expected",
    [
        ("Hello {name}", {"name": "Alice"}, None, "Hello Alice"),
        ("{x} + {y}", {"x": 1, "y": 2}, True, "1 + 2"),
        ("{x}", {"x": "skip"}, False, None),
    ],
)
def test_format(template, context, when, expected):
    assert Format(template, when=when).render(context) == expected
