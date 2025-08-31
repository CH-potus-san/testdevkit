# Defaults for element parameters will be set here and instance calls will pass their
# settings through these templates to the Kivy widgets with added customization functionality.

from TDKivy import TDKBoxLayout, TDKEmptySpacer, add_widgets
from TDKivy.buttons.launch import TDKLaunchButton
from TDKivy.labels.launch import TDKHeaderLabel, TDKFooterLabel

# Elements will be roughly ordered from the inside out


class TDKLaunchHeaderLayout(TDKBoxLayout):
    def __init__(
        self,
        orientation="vertical",
        spacing=20,
        padding=15,
        size_hint=(1.0, 0.66),
        **kwargs,
    ):
        super().__init__(
            **kwargs,
            size_hint=size_hint,
            padding=padding,
            spacing=spacing,
            orientation=orientation,
        )

        self._header_label = TDKHeaderLabel()

        with self.canvas:
            self.add_widget(self.header_label)

    @property
    def header_label(self):
        return self._header_label


class TDKLaunchButtonCreditsLayout(TDKBoxLayout):
    # This will get old but there will be open ports to change these options everywhere
    def __init__(self, orientation="horizontal", **kwargs):
        super().__init__(**kwargs, orientation=orientation)

        self.credit_button_spacer = lambda: TDKEmptySpacer(size_hint=(0.3, 1))
        self._button_credits = TDKLaunchButton(
            txt="Credits & Thanks", bg_color_down=(0.6, 1, 0.6, 1)
        )

        with self.canvas:
            add_widgets(self, [self.credit_button_spacer(), self.button_credits, self.credit_button_spacer()])

    @property
    def button_credits(self):
        return self._button_credits


class TDKLaunchButtonActionsLayout(TDKBoxLayout):
    def __init__(self, orientation="horizontal", **kwargs):
        super().__init__(**kwargs, orientation=orientation)

        self._button_options = TDKLaunchButton(
            txt="Display Options",
        )
        self._action_spacer = TDKEmptySpacer(size_hint=(0.3, 1.0))
        self._button_login = TDKLaunchButton(
            txt="Author Login",
        )

        with self.canvas:
            add_widgets(
                self, [self.button_login, self.action_spacer, self.button_options]
            )

    @property
    def button_login(self):
        return self._button_login

    @property
    def action_spacer(self):
        return self._action_spacer

    @property
    def button_options(self):
        return self._button_options


class TDKLaunchButtonsZoneLayout(TDKBoxLayout):
    def __init__(
        self,
        rounded=True,
        bg_color=(0.2, 0.2, 0.2, 0.6),
        orientation="vertical",
        **kwargs,
    ):
        super().__init__(
            **kwargs,
            rounded=rounded,
            bg_color=bg_color,
            orientation=orientation,
        )
        # Widgets added to layouts should be accessible as properties of the layout if possible
        self._button_credits_layout = TDKLaunchButtonCreditsLayout()
        self._button_actions_layout = TDKLaunchButtonActionsLayout()

        with self.canvas:
            self.add_widget(self.button_credits_layout)
            self.add_widget(self.button_actions_layout)

    @property
    def button_credits_layout(self):
        return self._button_credits_layout

    @property
    def button_actions_layout(self):
        return self._button_actions_layout


class TDKLaunchButtonsLayout(TDKBoxLayout):
    def __init__(
        self,
        bg_color=(0.2, 0.2, 0.2, 0.0),
        size_hint=(1, 0.66),
        orientation="horizontal",
        **kwargs,
    ):
        super().__init__(
            **kwargs,
            bg_color=bg_color,
            size_hint=size_hint,
            orientation=orientation,
        )
        self.button_zone_spacer = lambda: TDKEmptySpacer(size_hint=(0.3, 1))
        self._button_zone_layout = TDKLaunchButtonsZoneLayout()

        with self.canvas:
            add_widgets(
                self,
                [
                    self.button_zone_spacer(),
                    self.button_zone_layout,
                    self.button_zone_spacer(),
                ],
            )

    @property
    def button_zone_layout(self):
        return self._button_zone_layout


class TDKLaunchFooterLayout(TDKBoxLayout):
    def __init__(self, bg_color=(1, 1, 1, 1), orientation="vertical", size_hint=(1.0, 0.2), **kwargs):
        super().__init__(orientation=orientation, size_hint=size_hint, bg_color=bg_color, **kwargs)
        
        self._footer_spacer_top = TDKEmptySpacer()
        self._footer_spacer_left = TDKEmptySpacer()
        self._footer_spacer_right = TDKEmptySpacer()
        self._footer_compressor = TDKEmptySpacer(orientation="horizontal")
        self._footer = TDKFooterLabel(size_hint=(0.3, 0.2))

        with self.canvas:
            add_widgets(self.footer_compressor, [self.footer_spacer[1], self.footer, self.footer_spacer[2]])
            add_widgets(self, [self.footer_spacer[0], self.footer_compressor])

    @property
    def footer_compressor(self):
        return self._footer_compressor
    
    @property
    def footer_spacer(self):
        return [self._footer_spacer_top, self._footer_spacer_left, self._footer_spacer_right]
    
    @property
    def footer(self):
        return self._footer
    

class TDKLaunchLayout(TDKBoxLayout):
    # Set relevant parameter defaults here
    def __init__(
        self,
        orientation="vertical",
        bg_src=None,  # "./screens/source/launch.png",
        bg_color=(0.0, 0.0, 0.0, 1),
        rounded=True,
        spacing=15,
        padding=10,
        size_hint_min=(1.0, 0.3),
        **kwargs,
    ):
        """Layout for the launch screen. Pass >>>all<<< relevant instancing config arguments through these templates"""
        # Pass relevant parameters above to the parent class like a baton with unexpected changes
        super().__init__(
            orientation=orientation,
            bg_src=bg_src,
            bg_color=bg_color,
            rounded=rounded,
            spacing=spacing,
            padding=padding,
            size_hint_min=size_hint_min,
            **kwargs,
        )
        self._header_layout = TDKLaunchHeaderLayout()
        self._content_spacer = TDKEmptySpacer(size_hint=(1.0, 1.0))
        self._buttons_layout = TDKLaunchButtonsLayout()
        self._footer_layout = TDKLaunchFooterLayout()

        with self.canvas:
            add_widgets(
                self, [self.header_layout, self.content_spacer, self.buttons_layout, self.footer_layout]
            )

    @property
    def header_layout(self):
        return self._header_layout

    @property
    def content_spacer(self):
        return self._content_spacer

    @property
    def buttons_layout(self):
        return self._buttons_layout
    
    @property
    def footer_layout(self):
        return self._footer_layout
