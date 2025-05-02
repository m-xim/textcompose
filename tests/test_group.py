from textcompose.container.group import Group
from textcompose.content.text import Text


def test_group_render_with_separator():
    text1 = Text("One")
    text2 = Text("Two")
    group = Group(text1, text2, sep=", ")

    result = group.render({})
    assert result == "One, Two"


def test_group_render_with_conditions():
    text1 = Text("Visible", when=True)
    text2 = Text("Hidden", when=False)
    group = Group(text1, text2)

    result = group.render({})
    assert result == "Visible"
