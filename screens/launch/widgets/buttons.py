from screens import TDKButton

class TDKLaunchButton(TDKButton):
    def __init__(self, txt='button', **kwargs):
        super().__init__(
            **kwargs,
            rounded=True,
            bg_color=(0.9, 0.8, 0.75, 1),
            bg_color_down=(0.75, 0.5, 0.9, 1),
            bg_src="./screens/source/button.png",
            fg_color=(0.8, 0.65, 0.65, .8),
            fg_color_down=(0.5, 0.35, 0.35, 1),
            fg_src="./screens/source/buttborder.png",      
            text=txt,
            bold=True, 
            size_hint_min=(0.33, 0.5),
            size_hint= (0.45, 0.75),
            )
        