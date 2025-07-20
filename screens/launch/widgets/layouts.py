# Defaults for element parameters will be set here and instance calls will pass their
# settings through these templates to the Kivy widgets with added customization functionality.
from screens import TDKBoxLayout
from screens.launch.widgets.buttons import TDKLaunchButton
from screens.launch.widgets.labels import TDKHeaderLabel

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

        self._button_credits = TDKLaunchButton(
            txt="Credits & Thanks", bg_color_down=(0.6, 1, 0.6, 1)
        )

        with self.canvas:
            self.add_widget(self.button_credits)

    @property
    def button_credits(self):
        return self._button_credits


class TDKLaunchButtonActionsLayout(TDKBoxLayout):
    def __init__(self, orientation="horizontal", **kwargs):
        super().__init__(**kwargs, orientation=orientation)

        self._button_options = TDKLaunchButton(
            txt="Display Options",
        )
        self._button_login = TDKLaunchButton(
            txt="Author Login",
        )

        with self.canvas:
            self.add_widget(self.button_login)
            self.add_widget(self.button_options)

    @property
    def button_login(self):
        return self._button_login

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

        self._button_zone_layout = TDKLaunchButtonsZoneLayout()

        with self.canvas:
            self.add_widget(self.button_zone_layout)

    @property
    def button_zone_layout(self):
        return self._button_zone_layout


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
        self._buttons_layout = TDKLaunchButtonsLayout()

        with self.canvas:
            self.add_widget(self.header_layout)
            self.add_widget(self.buttons_layout)

    @property
    def header_layout(self):
        return self._header_layout

    @property
    def buttons_layout(self):
        return self._buttons_layout
