from textcompose.template import Template
from textcompose.content.text import Text


def test_template_render_multiple_components():
    text1 = Text("Component 1")
    text2 = Text("Component 2")
    template = Template(text1, text2)

    result = template.render({})
    assert result == "Component 1\nComponent 2"


def test_template_render_empty():
    template = Template()
    result = template.render({})
    assert result == ""


def test_template_with_conditions():
    text1 = Text("Visible", when=True)
    text2 = Text("Hidden", when=False)
    template = Template(text1, text2)

    result = template.render({})
    assert result == "Visible"


def test_template_with_dynamic_condition():
    text1 = Text("Dynamic", when=lambda context: context.get("show", False))
    template = Template(text1)

    result = template.render({"show": True})
    assert result == "Dynamic"

    result = template.render({"show": False})
    assert result == ""
