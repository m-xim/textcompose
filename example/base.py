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
