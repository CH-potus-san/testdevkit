from screens import TDKButton


class TDKLaunchButton(TDKButton):
    def __init__(
        self,
        txt="button",
        rounded=True,
        bold=True,
        size_hint_min=(0.33, 0.5),
        size_hint=(0.45, 0.75),
        bg_src="./screens/source/button.png",
        fg_src="./screens/source/buttborder.png",
        **kwargs
    ):
        super().__init__(
            rounded=rounded,
            bg_src=bg_src,
            fg_src=fg_src,
            text=txt,
            bold=bold,
            size_hint_min=size_hint_min,
            size_hint=size_hint,
            **kwargs,
        )
