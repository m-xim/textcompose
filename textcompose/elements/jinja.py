from jinja2 import Environment, BaseLoader, select_autoescape

from textcompose.core import Condition, Value
from textcompose.elements.base import Element

TEXTCOMPOSE_JINJA_ENV_FIELD = "textcompose_jinja_env"


class Jinja(Element):
    def __init__(self, template: Value, when: Condition | None = None):
        self.template = template
        super().__init__(when=when)

    def render(self, context, **kwargs) -> str:
        if TEXTCOMPOSE_JINJA_ENV_FIELD in kwargs:
            env = kwargs[TEXTCOMPOSE_JINJA_ENV_FIELD]
        else:
            kwargs[TEXTCOMPOSE_JINJA_ENV_FIELD] = default_env
            env = default_env

        template = env.get_template(self.template)

        return template.render(context)


class StubLoader(BaseLoader):
    def get_source(self, environment, template):
        del environment  # unused
        return template, template, lambda: True


def _create_env(*args, filters=None, **kwargs) -> Environment:
    env = Environment(loader=StubLoader(), autoescape=select_autoescape(["html", "xml"]), *args, **kwargs)

    if filters:
        env.filters.update(filters)

    return env


default_env = _create_env()
