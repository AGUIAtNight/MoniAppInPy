import kivy
from kivy.app import App

from kivy.lang import Builder

kv = '''
BoxLayout:
    Button:
        text: 'Click Me'
'''

Builder.load_string(kv)

class MyApp(App):
    def build(self):
        return Builder.load_string(kv)
    
if __name__ == '__main__':
    MyApp().run()    