from textcompose.logics.if_then_else import If


def test_renders_then_when_condition_true():
    content = If(if_=lambda ctx: True, then_="Yes", else_="No")
    result = content.render({})
    assert result == "Yes"


def test_renders_else_when_condition_false():
    content = If(if_=lambda ctx: False, then_="Yes", else_="No")
    result = content.render({})
    assert result == "No"


def test_returns_none_when_when_condition_is_false():
    content = If(if_=lambda ctx: True, then_="Yes", else_="No", when=lambda ctx: False)
    result = content.render({})
    assert result is None


def test_renders_then_with_context_passed():
    content = If(if_=lambda ctx: ctx.get("flag"), then_=lambda ctx: ctx["value"], else_="No")
    result = content.render({"flag": True, "value": "ContextValue"})
    assert result == "ContextValue"


def test_renders_else_when_then_is_none():
    content = If(if_=lambda ctx: False, then_=None, else_="Fallback")
    result = content.render({})
    assert result == "Fallback"


def test_returns_none_when_both_then_and_else_are_none():
    content = If(if_=lambda ctx: False, then_=None, else_=None)
    result = content.render({})
    assert result is None


def test_handles_non_callable_then_and_else():
    content = If(if_=True, then_=123, else_=456)
    result = content.render({})
    assert result == 123
