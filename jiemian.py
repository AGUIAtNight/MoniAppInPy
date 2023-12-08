# import kivy
# from kivy.app import App

# from kivy.lang import Builder

# kv = '''
# BoxLayout:
#     Button:
#         text: 'Click Me'
# '''

# Builder.load_string(kv)

# class MyApp(App):
#     def build(self):
#         return Builder.load_string(kv)
    
# if __name__ == '__main__':
#     MyApp().run()    


from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from bottom_buttons import BottomButtons

class MainApp(App):
   def build(self):
       root = BoxLayout()
       bottom_buttons = BottomButtons()
       root.add_widget(bottom_buttons)
       return root

if __name__ == '__main__':
   MainApp().run()