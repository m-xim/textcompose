from dataclasses import dataclass

from textcompose.core import Value


@dataclass
class ProgressBarStyle:
    """
    Configuration for customizing the appearance of a progress bar.

    Attributes:
        left (str | Value): Character or value for the left border.
        fill (str | Value): Character or value for the filled portion.
        empty (str | Value): Character or value for the empty portion.
        right (str | Value): Character or value for the right border.
        template (str): Format string for rendering the progress bar.

            Defaults to "{left}{bar}{right} {percent}".

            Supported placeholders:
                - {left}: Left border.
                - {bar}: Combined filled and empty segments.
                - {right}: Right border.
                - {percent}: Progress percentage (e.g., "50%").
                - {total}: Total number of steps.
                - {current}: Current step number.

    Built-in styles:
        Several built-in progress bar styles are available in the `PROGRESS_BAR_STYLES` dictionary
        defined in this file. To use a built-in style, simply specify its name (string key).
        For example:

            style = "symbol_square"

        See the `PROGRESS_BAR_STYLES` dictionary in this file for the full list of available style names.
    """

    left: str | Value
    fill: str | Value
    empty: str | Value
    right: str | Value
    template: str = "{left}{bar}{right} {percent}"


PROGRESS_BAR_STYLES = {
    # Symbol styles
    "symbol_square": ProgressBarStyle(left="[", fill="■", empty=" ", right="]"),
    "symbol_simple": ProgressBarStyle(left="[", fill="=", empty=" ", right="]"),
    "symbol_modern": ProgressBarStyle(left="|", fill="█", empty=" ", right="|"),
    "symbol_classic": ProgressBarStyle(left="[", fill="#", empty="-", right="]"),
    "symbol_block": ProgressBarStyle(left="[", fill="█", empty="░", right="]"),
    "symbol_arrow": ProgressBarStyle(left="|", fill="=", empty="-", right=">"),
    "symbol_circle": ProgressBarStyle(left="(", fill="●", empty="○", right=")"),
    "symbol_bracket": ProgressBarStyle(left="<", fill="#", empty=".", right=">"),
    "symbol_star": ProgressBarStyle(left="[", fill="★", empty="☆", right="]"),
    "symbol_magic": ProgressBarStyle(left="{", fill="▓", empty="░", right="}"),
    "symbol_line": ProgressBarStyle(left="[", fill="=", empty=" ", right="]"),
    "symbol_pipe": ProgressBarStyle(left="|", fill="█", empty=" ", right="|"),
    # Emoji styles
    "emoj_square": ProgressBarStyle(left="", fill="🟩", empty="⬜", right=""),
    "emoji_circle": ProgressBarStyle(left="", fill="🟢", empty="⚪", right=""),
}
