#Some screens may have context-sensitive pages that will open and close frequently.
#For instance, the credits screen will only be present for as long as the scrawl takes to complete
#Data from a pre-launch options menu may need to be delivered to the startup sequence after login
#Some page layouts may be used multiple times; rendering those unique pages will be handled here
from kivy.uix.screenmanager import Screen
from screens.launch.layouts.TDKLaunch import TDKLaunchLayout



class TDKScreenLaunch(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._launch_layout = TDKLaunchLayout()
        self._credits_layout = None
        self._options_layout = None
        self._login_layout = None

        self.add_widget(self.launch_layout)

    @property
    def launch_layout(self):
        return self._launch_layout

    @property
    def credits_layout(self):
        return self._credits_layout

    @property
    def options_layout(self):
        return self._options_layout

    @property
    def login_layout(self):
        return self._login_layout
