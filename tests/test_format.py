import pytest
from textcompose.content.format import Format


def test_format_basic_render():
    format_content = Format("Hello, {name}!")
    result = format_content.render({"name": "Alice"})
    assert result == "Hello, Alice!"


def test_format_missing_key():
    format_content = Format("Hello, {name}!")
    with pytest.raises(KeyError):
        format_content.render({})


def test_format_with_condition():
    format_content = Format("Conditional", when=lambda context: context.get("render", False))
    result = format_content.render({"render": True})
    assert result == "Conditional"

    result = format_content.render({"render": False})
    assert result is None
