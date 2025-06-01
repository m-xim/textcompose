import pytest

from textcompose.container.group import Group


@pytest.mark.parametrize(
    "children,sep,when,context,expected",
    [
        (["a", "b", "c"], ",", None, {}, "a,b,c"),
        (["x", None, "y"], "-", True, {}, "x-y"),
        (["1", "2"], "|", False, {}, None),
    ],
)
def test_group(children, sep, when, context, expected):
    group = Group(*children, sep=sep, when=when)
    assert group.render(context) == expected
