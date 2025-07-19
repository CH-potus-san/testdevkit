from screens import TDKLabel


class TDKHeaderLabel(TDKLabel):
    def __init__(
        self,
        bg_color=(.99, .99, .99, .6),
        fg_src='./screens/source/buttborder.png',
        fg_color=(.5, .4, .4, .3),
        rounded=True,
        **kwargs
    ):
        super().__init__(
            fg_src=fg_src,
            bg_color=bg_color,
            fg_color=fg_color,
            rounded=rounded,
            **kwargs
        )
