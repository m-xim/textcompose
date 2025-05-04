# TextCompose

[![PyPI version](https://img.shields.io/pypi/v/textcompose?color=blue)](https://pypi.org/project/textcompose)
[![License](https://img.shields.io/github/license/m-xim/textcompose.svg)](/LICENSE)
[![Tests Status](https://github.com/m-xim/textcompose/actions/workflows/tests.yml/badge.svg)](https://github.com/m-xim/textcompose/actions)
[![Release Status](https://github.com/m-xim/textcompose/actions/workflows/release.yml/badge.svg)](https://github.com/m-xim/textcompose/actions)

**TextCompose** is a Python library for creating dynamic, structured text templates. Inspired by [aiogram-dialog](https://github.com/Tishka17/aiogram_dialog), it provides a flexible and intuitive interface for composing text.

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

`TextCompose` provides the following core components:

1. **`Template`**: Combines and renders components as a structured text block.
2. **`Group`**: Groups multiple components and joins their output with a separator (`sep`).
3. **`Text`**: Displays static text.
4. **`Format`**: Formats strings dynamically using a given context.

All components support the `when` parameter for conditional rendering. If `when` evaluates to `True`, the component is rendered; otherwise, it is skipped.

### Example

Below is an example of how to use `TextCompose` to create dynamic text templates with nested components and conditional rendering.

```python
from textcompose import Template
from textcompose.container import Group
from textcompose.content import Format, Text

# Create a template using nested components
template = Template(
    Group(
        Format("Hello, {name}!"),
        Format("Your status: {status}."),
        Group(
            Text("You have new notifications."),
            Format("Notification count: {notifications}.", when=lambda ctx: ctx.get("notifications") > 0),
            sep=" "  # Separator for the nested group
        ),
        sep="\n"  # Separator for the main group
    )
)

# Context for rendering
context = {
    "name": "John",
    "status": "Online",
    "notifications": 3
}

# Render text
result = template.render(context)
print(result)
```

### Output:
```
Hello, John!
Your status: Online.
You have new notifications. Notification count: 3.
```

---

## 👨‍💻 Contributing

We welcome contributions to `TextCompose`. If you have suggestions or improvements, please open an issue or submit a pull request.