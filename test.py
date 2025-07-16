from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from screens.launch import TDKScreenLaunch

class TestDevKit(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(TDKScreenLaunch())
        return sm
    

if __name__ == '__main__':
    TestDevKit().run()
