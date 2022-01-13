# #kivy
import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from Notifier import Notifier
from Schedule import Schedule

Window.size = (750, 450)

# class Screen(Widget):
#     pass #it means that is not implemented yet, but i want to implement in future

kv = Builder.load_file("AppDesign.kv")

class MyApp(App):
    schedule = Schedule()

    def build(self):
        return kv
        # return Button (text = "         Ustaw \n przypomnienie",
        #                font_size = "18sp",
        #                background_color = (0, 0, 1, 1),
        #                color = (1, 1, 1, 1),
        #                size = (100,25),
        #                size_hint=(.18, .08),
        #                pos = (300, 500),
        #                pos_hint = {'center_x': 0.2, 'center_y': 0.1},
        #                on_press = self.pressButton,
        #                on_release = self.releaseButton)

    def pressButtonUstawPrzypomnienie(self, *args):
        print("Przycik został wciśnięty")
        # schedule = Schedule()
        # schedule.setTime()

        notifier = Notifier()
        notifier.getReminderAbMedicines()

    def pressButton(self, *args):
        print("Przycik został wciśnięty")

    def releaseButton(self, *args):
        print("Przycik został puszczony")

    # def button2(self):
    #     return Button(text="Kalendarz",
    #                      font_size="18sp",
    #                      background_color=(0, 0, 1, 1),
    #                      color=(1, 1, 1, 1),
    #                      size=(100, 25),
    #                      size_hint=(.18, .08),
    #                      pos=(300, 500),
    #                      pos_hint={'center_x': 0.5, 'center_y': 0.1})

MyApp().run()
