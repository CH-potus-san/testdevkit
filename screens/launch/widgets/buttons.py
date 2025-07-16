from screens import TDKButton

class TDKLaunchButton(TDKButton):
    def __init__(self, txt='button', **kwargs):
        super().__init__(
            **kwargs,
            bg_color=(0.5, 0.5, 0.5, 1.0),      
            font_size=f"{self.width/5}pt", 
            bold=True, 
            size_hint_min=(0.33, 0.5),
            size_hint= (0.45, 0.75),
            text=txt
            )
        