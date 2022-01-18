from kivy.app import App
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.picker import MDDatePicker, MDTimePicker
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window

from Notifier import Notifier
from Reminder import Reminder

from matplotlib import pyplot as plt
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg

import csv

Window.size = (750, 450)


class PlotWindow(Screen):
    def plotFunction(self):
        x = [10, 11, 12, 13, 14, 15]
        y = [98, 87, 67, 78, 90, 103]

        plt.plot(x, y, color='r', linestyle='--', marker='.')
        plt.xlabel("Date")
        plt.ylabel("Pulse")

        box = self.ids.box
        box.add_widget(FigureCanvasKivyAgg(plt.gcf()))


class SecondWindow(Screen):
    def pressButtonZatwierdz(self):
        myGUI = MyGUI()
        myGUI.show_date_picker()

        messageTitle = self.ids.msgTitle.text
        message = self.ids.msg.text
        myGUI.func(messageTitle, message)
        print("tit and mess: ", messageTitle, message)


class MainWindow(Screen):
    pass


class ListWindow(Screen):
    pass


class AddPulse(Screen):
    def savePlot(self):
        # name = self.ids.namer.text
        # if name:
        #     plt.savefig(name)

        pulseValue = self.ids.pulseValue.text
        print(pulseValue)

        with open('PulseDate.csv', 'w', newline='') as csvFile:
            writer = csv.writer(csvFile, quoting=csv.QUOTE_NONNUMERIC, delimiter=';')
            writer.writerow(pulseValue)

        # csvFile = open("PulseDate.csv", 'w', newline=' ')
        # writer = csv.writer(csvFile)
        # writer.writerow('65')
        # csvFile.close()


class WindowManager(ScreenManager):
    pass

# Builder.load_string("""
# <MainWindow>:
#     BoxLayout:
#         Button:
#             text: 'Goto settings'
#             on_press: root.manager.current = 'settings'
#         Button:
#             text: 'Quit'
#
# <SecondWindow>:
#     BoxLayout:
#         Button:
#             text: 'My settings button'
#         Button:
#             text: 'Back to menu'
#             on_press: root.manager.current = 'menu'
# """)


class MyGUI(MDApp):
    notifier = Notifier()
    sm = None

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"

        self.sm = Builder.load_file("AppDesign.kv")
        return self.sm

    def func(self, msgTitle, msg):
        self._msgTitle = msgTitle
        self._msg = msg

    def callback(self):
        print("messageTitle and message: ", self._msgTitle, self._msg)
        self.notifier.notify(self._msgTitle, self._msg)

    def save_time(self, instance, time):
        reminder = Reminder(str(time), self.callback)
        print(str(time))

    def cancel_time(self, instance, time):
        print("You clicked cancel!")

    def show_time_picker(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        from datetime import datetime
        time_dialog = MDTimePicker()
        time_dialog.bind(on_save=self.save_time, on_cancel=self.cancel_time)
        time_dialog.open()

    # dodawanie przypomnienia w przedziale czasowym!!
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

    def presser(self, pressed, list_id):
        pressed.text = f"You pressed {list_id}"