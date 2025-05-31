# TextCompose

[![PyPI version](https://img.shields.io/pypi/v/textcompose?color=blue)](https://pypi.org/project/textcompose)
[![License](https://img.shields.io/github/license/m-xim/textcompose.svg)](/LICENSE)
[![Tests Status](https://github.com/m-xim/textcompose/actions/workflows/tests.yml/badge.svg)](https://github.com/m-xim/textcompose/actions)
[![Release Status](https://github.com/m-xim/textcompose/actions/workflows/release.yml/badge.svg)](https://github.com/m-xim/textcompose/actions)
[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/m-xim/textcompose)

**TextCompose** is a Python library for creating dynamic, structured text templates. Inspired by [aiogram-dialog](https://github.com/Tishka17/aiogram_dialog), it provides a flexible and intuitive interface for composing text.

---

## ✨ Features

- Flexible text composition from components
- Conditional rendering support (`when`)
- Grouping and repeating blocks
- Formatting via f-string and Jinja2
- Easily extensible with new components

---

## 🚀 Installation

You can install the library in two ways:

### Using `uv`
If you are using the `uv` package manager, you can install it as follows:
```bash
uv add textcompose
```

### Using `pip`
```bash
pip install textcompose
```

---


## 💻 Usage

### Components Overview

#### General

- `Template` — combines and renders components as a structured text block.

#### Content Blocks

- `BaseContent` — abstract base class for all content components


- `Text` — outputs static text
- `Format` — dynamic formatting via f-string
- `Jinja` — rendering via Jinja2 templates

#### Containers

- `BaseContainer` — abstract base class for containers


- `Group` — groups children with a separator
- `List` — repeats a template for a collection

#### Logic Components

- `If` — conditional rendering (`if_`, `then_`, `else_`)

All components support the `when` parameter for conditional rendering.

---

## 📝 Example

```python
from magic_filter import F

from textcompose import Template
from textcompose.container import Group, List
from textcompose.content import Format, Text, Jinja
from textcompose.logic import If

template = Template(
    Format("Hello, {name}!"),
    Format("Status: {status}"),  # or `lambda ctx: f"Status: {ctx['status']}"` with function
    If(
        F["notifications"] > 0,  # `if_` - condition to check if there are notifications
        Format("You have {notifications} new notifications."),  # `then_` - content to render if condition is True
        Format("You not have new notifications."),  # `else_` - content to render if condition is False
    ),
    Group(
        Jinja("\nTotal messages {{ messages|length }}:"),
        List(
            Format("Time - {item[time]}:"),
            Format("-  {item[text]}"),
            sep="\n",  # `sep` - separator between list items
            inner_sep="\n",  # `inner_sep` - separator between parts of a single item
            getter=lambda ctx: ctx["messages"],  # `getter` - function or F to extract the list of messages from context
        ),
        sep="\n",  # `sep` - separator between children of Group
        when=F["messages"].len() > 0,  # `when` - show this block only if there are messages
    ),
    Text("\nThank you for using our service!"),  # or "Recent messages:" without class
)

context = {
    "name": "Alexey",
    "status": "Online",
    "notifications": 2,
    "messages": [
        {"text": "Your package has been delivered.", "time": "09:15"},
        {"text": "Reminder: meeting tomorrow at 10:00.", "time": "18:42"},
    ],
}

print(template.render(context))
```

**Output:**
```
Hello, Alexey!
Status: Online
You have 2 new notifications.

Total messages 2:
Time - 09:15:
-  Your package has been delivered.
Time - 18:42:
-  Reminder: meeting tomorrow at 10:00.

Thank you for using our service!
```

---

## 👨‍💻 Contributing

We welcome contributions to `TextCompose`. If you have suggestions or improvements, please open an issue or submit a pull request.
