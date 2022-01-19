import datetime

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

from datetime import datetime
import csv

Window.size = (750, 450)


class PlotWindow(Screen):
    def pulsePlot(self):

        x = []
        y = []

        with open("PulseDate.csv", 'r') as file:
            csvReader = csv.reader(file, delimiter=';')
            header = next(csvReader)
            for row in csvReader:
                y.append(int(row[0]))
                x.append(row[1])
                print(row)

        fig, ax = plt.subplots(1,1,figsize=(15,5))
        ax.plot(x, y, color='r', linestyle='--', marker='.')
        ax.set_title('Puls')
        fig.patch.set_facecolor('xkcd:grey')
        ax.set_facecolor('xkcd:dark grey')
        # ax.set(xlabel='Data', ylabel='Puls')
        xticks = ax.get_xticks()
        if len(xticks) >= 10:
            ax.set_xticks(xticks[::len(xticks) // 5])  # set new tick positions
        ax.tick_params(axis='x', rotation=12, labelsize=7)  # set tick rotation

        box = self.ids.box
        box.clear_widgets()
        box.add_widget(FigureCanvasKivyAgg(plt.gcf()))

    def temperaturePlot(self):
        x = []
        y = []

        with open("TemperatureData.csv", 'r') as file:
            csvReader = csv.reader(file, delimiter=';')
            header = next(csvReader)
            for row in csvReader:
                y.append(float(row[0]))
                x.append(row[1])
                print(row)

        fig, ax = plt.subplots(1,1,figsize=(15,5))
        ax.plot(x, y, color='b', linestyle='--', marker='.')
        ax.set_title('Temperature')
        fig.patch.set_facecolor('xkcd:grey')
        ax.set_facecolor('xkcd:dark grey')
        # ax.set(xlabel='Data', ylabel='Puls')

        xticks = ax.get_xticks()

        if len(xticks) >= 10:
            ax.set_xticks(xticks[::len(xticks) // 5])  # set new tick positions

        ax.tick_params(axis='x', rotation=12, labelsize=7)  # set tick rotation

        box = self.ids.box
        box.clear_widgets()
        box.add_widget(FigureCanvasKivyAgg(plt.gcf()))

class SecondWindow(Screen):
    def pressButtonZatwierdz(self):
        myGUI = MyGUI()
        myGUI.show_date_picker()
        print(id(myGUI))

        messageTitle = self.ids.msgTitle.text
        message = self.ids.msg.text
        myGUI.func(messageTitle, message)
        print("tit and mess: ", messageTitle, message)


class MainWindow(Screen):
    pass


class ListWindow(Screen):
    pass


class PulseWindow(Screen):
    def addNewPulseValue(self):
        pulseValue = self.ids.pulseValue.text
        print("pulseValue:", pulseValue)
        print(type(pulseValue))

        if pulseValue is not '':
            with open('PulseDate.csv', 'a', newline='') as csvFile:
                writer = csv.writer(csvFile, delimiter=';')
                now = datetime.now()
                dateTime_string = now.strftime("%d/%m/%Y %H:%M")
                writer.writerow([int(pulseValue), dateTime_string])

    def addNewTemperatureValue(self):
        temperatureValue = self.ids.temperatureValue.text
        print(temperatureValue)

        if temperatureValue is not '':
            with open('TemperatureData.csv', 'a', newline='') as csvFile:
                writer = csv.writer(csvFile, delimiter=';')
                now = datetime.now()
                dateTime_string = now.strftime("%d/%m/%Y %H:%M")
                writer.writerow([float(temperatureValue), dateTime_string])


class WindowManager(ScreenManager):
    pass


class SingletonMeta(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):

        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class MyGUI(MDApp, metaclass=SingletonMeta):
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