from textcompose.core import Condition, Value, resolve_value
from textcompose.elements.base import Element
from textcompose.styles.progress_bar import PROGRESS_BAR_STYLES, ProgressBarStyle


class ProgressBar(Element):
    def __init__(
        self,
        current: Value,
        total: Value = 100,
        width: Value | int = 20,
        style: Value | ProgressBarStyle = "emoj_square",
        when: Condition | None = None,
    ):
        super().__init__(when=when)
        self.current = current
        self.total = total
        self.width = width
        self.style = style
        self.when = when

    def render(self, context, **kwargs) -> str | None:
        if not self._check_when(context, **kwargs):
            return None

        if isinstance(self.style, str):
            style_obj = PROGRESS_BAR_STYLES.get(self.style, None)
        else:
            style_obj = ProgressBarStyle(
                left=resolve_value(self.style.left, context),
                fill=resolve_value(self.style.fill, context),
                empty=resolve_value(self.style.empty, context),
                right=resolve_value(self.style.right, context),
            )
            if self.style.template is not None:
                style_obj.template = resolve_value(self.style.template, context)

        if style_obj is None:
            raise ValueError(f"Unknown style: {self.style}. Available styles: {', '.join(PROGRESS_BAR_STYLES.keys())}")

        length = int(resolve_value(self.width, context))
        if length <= 0:
            raise ValueError("Progress bar length must be a positive integer.")
        current = float(resolve_value(self.current, context))
        if current < 0:
            raise ValueError("Current value must be non-negative.")
        total = float(resolve_value(self.total, context))
        if total <= 0:
            raise ValueError("Total value must be greater than zero.")

        percent = min(max(current / total, 0), 1)
        filled_len = int(round(length * percent))
        empty_len = length - filled_len

        bar_str = (style_obj.fill * filled_len) + (style_obj.empty * empty_len)

        return style_obj.template.format(
            left=style_obj.left,
            bar=bar_str,
            right=style_obj.right,
            percent=f"{int(percent * 100)}%",
            total=total,
            current=current,
        )
