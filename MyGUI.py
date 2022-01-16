from kivy.app import App
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.theming import ThemeManager
from kivymd.uix.picker import MDDatePicker, MDTimePicker
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window

from Notifier import Notifier
from Reminder import Reminder

Window.size = (750, 450)


class SecondWindow(Screen):
    pass


class PlotWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass


class MyGUI(MDApp):

    notifier = Notifier()

    def build(self):
        return Builder.load_file("AppDesign.kv")

    def callback(self):
        self.notifier.notify("Przypomnienie o lekach", "Wez leki")

    def save_time(self, instance, time):
        reminder = Reminder(str(time), self.callback)
        print(str(time))

    def cancel_time(self, instance, time):
        print("You clicked cancel!")

    def show_time_picker(self):
        from datetime import datetime
        time_dialog = MDTimePicker()
        time_dialog.bind(on_save=self.save_time, on_cancel=self.cancel_time)
        time_dialog.open()

    def save_date(self, instance, value, date_range):
        # print(instance, value, date_range)
        print(str(value))
        # self.root.ids.date_label.text = str(value)
        # self.root.ids.date_label.text = f'{str(date_range[0])} - {str(date_range[-1])}'
        self.show_time_picker()

    def cancel_date(self, instance, value):
        print("You clicked cancel!")

    def show_date_picker(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        date_dialog = MDDatePicker(mode="range")
        date_dialog.bind(on_save=self.save_date, on_cancel=self.cancel_date)
        date_dialog.open()


class MainWindow(Screen, MyGUI):
    pass

