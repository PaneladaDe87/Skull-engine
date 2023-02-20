from kivy.app import App
from kivy.lang import Builder

GUI = Builder.load_file("tela1.kv")

class SkullEngine(App):
    def build(self):
        return GUI
        
SkullEngine().run()
