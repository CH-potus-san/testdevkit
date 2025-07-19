from screens import TDKLabel


class TDKHeaderLabel(TDKLabel):
    def __init__(
        self,
        bg_color=(.66, .66, .66, .66),
        padding=15,
        rounded=True,
        **kwargs
    ):
        super().__init__(
            bg_color=bg_color,
            padding=padding,
            rounded=rounded,
            **kwargs
        )
