from kivy.app import App
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.picker import MDDatePicker, MDTimePicker
from kivymd.theming import ThemeManager


from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window

Window.size = (750, 450)


class MainWindow(Screen):

    def pressButtonUstawPrzypomnienie(self, *args):
        print("Przycik został wciśnięty")

        cal = Calendar()
        cal.show_date_picker()


class SecondWindow(Screen):
    pass


class PlotWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("AppDesign.kv")

class Calendar(MDApp):

    def saveTime(self, instance, time):
        print(str(time))

    def cancelTime(self, instance, time):
        print("You clicked cancel!")

    def show_time_picker(self):
        from datetime import datetime
        time_dialog = MDTimePicker()
        time_dialog.bind(on_save=self.saveTime, on_cancel=self.cancelTime)
        time_dialog.open()

    def on_save(self, instance, value, date_range):
        # print(instance, value, date_range)
        print(str(value))
        # self.root.ids.date_label.text = str(value)
        # self.root.ids.date_label.text = f'{str(date_range[0])} - {str(date_range[-1])}'
        self.show_time_picker()

    def on_cancel(self, instance, value):
        print("You clicked cancel!")

    def show_date_picker(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        date_dialog = MDDatePicker(mode="range")
        date_dialog.bind(on_save=self.on_save, on_cancel = self.on_cancel)
        date_dialog.open()

if __name__ == "main":
    Calendar().run()


class MyApp(App):

    def build(self):
        return kv

    def pressButton(self, *args):
        print("Przycik został wciśnięty")

    def releaseButton(self, *args):
        print("Przycik został puszczony")
MyApp().run()

