from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget

class BottomButtons(BoxLayout):
   def __init__(self, **kwargs):
       super(BottomButtons, self).__init__(**kwargs)

   def on_button_press(self, button_id):
       print(f'按钮{button_id}被点击了')