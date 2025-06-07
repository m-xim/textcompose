# TextCompose

[![PyPI version](https://img.shields.io/pypi/v/textcompose?color=blue)](https://pypi.org/project/textcompose)
[![License](https://img.shields.io/github/license/m-xim/textcompose.svg)](/LICENSE)
[![Tests Status](https://github.com/m-xim/textcompose/actions/workflows/tests.yml/badge.svg)](https://github.com/m-xim/textcompose/actions)
[![Release Status](https://github.com/m-xim/textcompose/actions/workflows/release.yml/badge.svg)](https://github.com/m-xim/textcompose/actions)
[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/m-xim/textcompose)

**TextCompose** is a Python library for creating dynamic, structured text templates with an intuitive, component-based approach. Inspired by [aiogram-dialog](https://github.com/Tishka17/aiogram_dialog).

---

## ✨ Features

- 🧱 Flexible text composition from components
- 🔀 Conditional rendering support (`when`)
- 🔁 Grouping and repeating blocks
- 🎨 Formatting via f-string and Jinja2
- 🔌 Easily extensible with new components

## 🚀 Installation

```bash
uv add textcompose
# or
pip install textcompose
```

## 🧩 Components Overview

### General

- `Template` — main class for combining and rendering components


### Elements
`Element` — abstract base class for all element components

- `Text` — static text.
- `Format` — dynamic python f-string formatting
- `Jinja` — Jinja2 template rendering
- [`ProgressBar`](#progressbar) — show progress visually

### Containers
`Container` — abstract base class for all container components

- `Group` — group children with custom separators.
- `List` — repeat templates for each item in a collection.

### Logic Components
`Logic` — abstract base class for all container components

- `If` — conditionally show different blocks (use `if_`, `then_`, `else_`)

> [!TIP]
> All components support the `when` parameter for conditional display (value, expression, function, or magic_filter).

## ⚡️ How to Use

All usage examples can be found in the [`example`](./example) folder.

### Quick Start
See how easy it is to build structured, interactive text blocks:

```python
from magic_filter import F

from textcompose import Template
from textcompose.containers import Group, List
from textcompose.elements import Format, Jinja, Text
from textcompose.logics import If

template = Template(
    Format("Hello, {name}!"),
    Format("Status: {status}"),  # or `lambda ctx: f"Status: {ctx['status']}"` with function
    If(
        F["notifications"] > 0,  # `if_`: condition to check if there are notifications
        Format("You have {notifications} new notifications."),  # `then_`: content to render if condition is True
        Format("You not have new notifications."),  # `else_`: content to render if condition is False
    ),
    Group(
        Jinja("\nTotal messages {{ messages|length }}:"),
        List(
            Format("Time - {item[time]}:"),
            Format("-  {item[text]}"),
            sep="\n",  # `sep`: separator between list items
            inner_sep="\n",  # `inner_sep`: separator between parts of a single item
            getter=lambda ctx: ctx["messages"],  # `getter`: function or F to extract the list of messages from context
        ),
        sep="\n",  # `sep`: separator between children of Group
        when=F["messages"].len() > 0,  # `when`: show this block only if there are messages
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

### ProgressBar

The `ProgressBar` component renders a textual progress bar. It supports various styles, customizable width, templates, and dynamic values.

#### Usage

```python
from textcompose.elements import ProgressBar

bar = ProgressBar(
    current=42,  # `current`: Current progress value
    total=100,  # `total`: Total value for the progress bar
    width=20,  # `width`: Number of characters in the bar.
    style="symbol_square",  # `style`: Style (string — built-in style name, or `ProgressBarStyle` object).
)
print(bar.render({}))
```

**Output:**
```
[■■■■■■■■        ] 42%
```

#### Styles

Built-in styles are listed in the `PROGRESS_BAR_STYLES` dictionary (see [`textcompose/styles/progress_bar.py`](./textcompose/styles/progress_bar.py)). Examples:

- `"symbol_square"`: `[■■■■■     ]`
- `"symbol_classic"`: `[#####-----]`
- `"emoj_square"`: `🟩🟩🟩⬜⬜⬜`
- `"emoji_circle"`: `🟢🟢⚪⚪⚪`

You can create a custom style using `ProgressBarStyle`:

```python
from textcompose.styles import ProgressBarStyle
from textcompose.elements import ProgressBar


custom_style = ProgressBarStyle(
    left="<", fill="*", empty="-", right=">", template="{percent} {left}{bar}{right}"
)
bar = ProgressBar(current=7, total=10, width=10, style=custom_style)
print(bar.render({}))
```

**Output:**
```
70% <*******--->
```

##### Template

The `template` parameter in the style allows you to customize the output string. Available placeholders:
- `{left}` — left border
- `{bar}` — the bar itself (filled + empty part)
- `{right}` — right border
- `{percent}` — percent complete (e.g., `42%`)
- `{total}` — maximum value
- `{current}` — current value

## 🤝 Contributing

💡 Ideas? Issues? PRs are welcome!<br>
Open an issue or pull request to help TextCompose get even better.

---

> **Ready to supercharge your text formatting?<br>**
> **Try TextCompose today and make your bots, reports, and notifications shine! ✨**