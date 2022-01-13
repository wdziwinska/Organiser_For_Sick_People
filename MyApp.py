# #kivy
import kivy
from kivy.app import App
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        return Button (text = "Ustaw przypomnienie",
                       font_size = "18sp",
                       background_color = (0, 0, 1, 1),
                       color = (1, 1, 1, 1),
                       size = (100,25),
                       size_hint = (.3,.15),
                       pos = (300, 500),
                       pos_hint = {'center_x': 0.5, 'center_y': 0.5})

MyApp().run()