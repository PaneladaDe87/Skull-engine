import kivy
from kivy.app import App
from kivy.uix.label import Label

class MainApp(App):
    def Build(self):
        return Label(text = "hello, world")

MainApp().run()
