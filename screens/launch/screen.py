from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle
from screens.launch.widgets.layouts import TDKLaunchButtonsRegionLayout, TDKLaunchLayout, TDKLaunchButtonsZoneLayout
from screens.launch.widgets.buttons import TDKLaunchButton

def add_widgets(layout, widgets):
    for widget in widgets:
        layout.add_widget(widget)

class TDKScreenLaunch(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Build the elements of the screen from the top down and from the inside out before putting it all together/
        # Build the full layout to stack the previous layouts on top of one another in
        self.layout = TDKLaunchLayout()
        headerLayout = BoxLayout(orientation="vertical", spacing=20, padding=15, size_hint=(1.0, 0.66))
        buttonZoneLayout = TDKLaunchButtonsZoneLayout()
        buttonCreditsLayout = BoxLayout(orientation="horizontal")
        buttonActionsLayout = BoxLayout(
            orientation="horizontal"
        )
        # Build the broader region these buttons will occupy
        buttonRegionLayout = TDKLaunchButtonsRegionLayout()
        licenseLabelLayout = BoxLayout(orientation="vertical", size_hint=(1, 0.33))


        # Build the Title and Version labels that will populate the header
        headerTitle = Label(text="Test Development Kit", font_size="40pt", bold=True)
        headerVersion = Label(text="Henkins0", font_size="20pt")
        # Build the layout the labels will lay on top of each other within.
        add_widgets(headerLayout, [headerTitle, headerVersion])

        # Build the spacers that will provide the window to whatever background art there happens to be
        def empty_spacer(hori=1.0, vert=1.0):
            return BoxLayout(orientation="horizontal", size_hint=(hori, vert))

        # Build the buttons, then build and fill the region of the layout with them
        buttonCredits = TDKLaunchButton(txt='Credits & Thanks')
        buttonLogin = TDKLaunchButton(txt='Author Login')
        buttonOptions = TDKLaunchButton(txt='Display Settings')
        # Build and fill the zone which contains the buttons
        add_widgets(buttonCreditsLayout, [empty_spacer(hori=0.33), buttonCredits, empty_spacer(hori=0.33)])
        buttonZoneLayout.add_widget(buttonCreditsLayout)
        # Keep the Login and Options buttons on the same row with another nested layout
        add_widgets(buttonActionsLayout, [empty_spacer(hori=0.05), buttonLogin, empty_spacer(hori=0.15), buttonOptions, empty_spacer(hori=0.05)])
        # Slide these buttons below the Credits button
        buttonZoneLayout.add_widget(buttonActionsLayout)
        # Stuff the buttons between some empty padding
        add_widgets(buttonRegionLayout, [empty_spacer(hori=0.33), buttonZoneLayout, empty_spacer(hori=0.33)])
        # Use a small empty spacer for the license info layout
        licenseLabel = Label(text="unlicensed so far", font_size="14pt", size_hint=(1.0, 0.01))
        licenseLabelLayout.add_widget(empty_spacer(vert=0.33))
        licenseLabelLayout.add_widget(licenseLabel)

        self.layout.add_widget(headerLayout)
        self.layout.add_widget(empty_spacer())
        self.layout.add_widget(buttonRegionLayout)
        self.layout.add_widget(licenseLabelLayout)
        # Add this to the screen for the ScreenManager
        self.add_widget(self.layout)
