from textcompose.content import Text


def test_text_static_render():
    text_content = Text("Simple text")
    result = text_content.render({})
    assert result == "Simple text"


def test_text_with_condition():
    text_content = Text("Conditional text", when=False)
    result = text_content.render({})
    assert result is None

    text_content = Text("Conditional text", when=True)
    result = text_content.render({})
    assert result == "Conditional text"
