#Some screens may have context-sensitive pages that will open and close frequently.
#For instance, the credits screen will only be present for as long as the scrawl takes to complete
#Data from a pre-launch options menu may need to be delivered to the startup sequence after login
#Some page layouts may be used multiple times; rendering those unique pages will be handled here
from kivy.uix.screenmanager import Screen
from screens.launch.widgets.layouts import TDKLaunchLayout


def add_widgets(layout, widgets):
    for widget in widgets:
        layout.add_widget(widget)


class TDKScreenLaunch(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = TDKLaunchLayout()

        self.add_widget(self.layout)
