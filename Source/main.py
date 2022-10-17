from kivy.app import App
from kivy.lang import Builder

kv = '''
floatLayout:
    Button:
        text: 'start'
        size_hint: none, none
        pos_hint: {'center_x 0.5', 'center_y 0.5'}
        canvas.before:
            PushMatrix:
                Rotate:
                    angle: 0
                    origin: self.center
        canvas.after:
            PopMatrix
'''
    

class menu(App):
    def build(self):
        return Builder.loadString(kv)

if __name__ == "__main__":
    menu().run()
