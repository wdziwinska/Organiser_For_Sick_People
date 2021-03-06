from datetime import datetime

from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.list import TwoLineListItem
from kivymd.uix.picker import MDDatePicker, MDTimePicker
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window

from Plots import Plots
from ReadCsvFile import ReadCsvFile
from Notifier import Notifier
from Reminder import Reminder

from matplotlib import pyplot as plt
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg

import csv

Window.size = (750, 450)
iterator = 0


class PlotWindow(Screen):
    def pulsePlot(self):

        x = []
        y = []

        csvFile = ReadCsvFile()
        x, y = csvFile.readFromPulseDate()

        plots = Plots()
        plots.drawPlot('Puls', x, y, 'r')

        self.showPlots()

    def temperaturePlot(self):
        x = []
        y = []

        csvFile = ReadCsvFile()
        x, y = csvFile.readFromTemperatureData()

        plots = Plots()
        plots.drawPlot('Temperatura', x, y, 'b')

        self.showPlots()

    def saturationPlot(self):
        x = []
        y = []

        csvFile = ReadCsvFile()
        x, y = csvFile.readFromSaturationData()

        plots = Plots()
        plots.drawPlot('Saturacja', x, y, 'g')

        self.showPlots()

    def showPlots(self):
        box = self.ids.box
        box.clear_widgets()
        box.add_widget(FigureCanvasKivyAgg(plt.gcf()))


class AddMessageWindow(Screen):
    def pressButtonZatwierdz(self):
        myGUI = MyGUI()
        myGUI.show_date_picker()
        # print(id(myGUI))

        messageTitle = self.ids.msgTitle.text
        message = self.ids.msg.text
        myGUI.func(messageTitle, message)
        print("Message Title and Message: ", messageTitle, ";", message)
        self.ids.msgTitle.text = ""
        self.ids.msg.text = ""


class MainWindow(Screen):
    def generateListOfMessage(self):
        listWindow = ListWindow()
        listWindow.messageForList()


class ListWindow(Screen):
    _iterator = iterator
    def messageForList(self):
        if self._iterator < 1:
            csvFile = ReadCsvFile()
            messageTitleTable, messageTable, counter = csvFile.readFromFileMessage()
            for i in range(counter):
                self.ids.item.add_widget(TwoLineListItem(text=messageTitleTable[i], secondary_text=messageTable[i], on_release=self.release))
            self._iterator = self._iterator + 1
        else:
            self.ids.item.clear_widgets()
            self._iterator = 0

    def release(self, onelinelistitem):
        self.ids.item.remove_widget(onelinelistitem)

        updatedlist = []
        with open("Message.csv", newline="", encoding='utf-8') as f:
            reader = csv.reader(f)
            clicked = onelinelistitem.text +";"+onelinelistitem.secondary_text

            for row in reader:
                if row[0] != clicked:
                    updatedlist.append(row)
            # print(updatedlist)
            self.updatefile(updatedlist)

    def updatefile(self, updatedlist):
        with open("Message.csv", "w", newline="", encoding='utf-8') as f:
            Writer = csv.writer(f)
            Writer.writerows(updatedlist)
            # print("File has been updated")


class AddDataWindow(Screen):
    def addNewPulseValue(self):
        pulseValue = self.ids.pulseValue.text
        print(pulseValue)

        if pulseValue is not '':
            with open('PulseDate.csv', 'a', newline='') as csvFile:
                writer = csv.writer(csvFile, delimiter=';')
                now = datetime.now()
                dateTime_string = now.strftime("%d/%m/%Y %H:%M")
                writer.writerow([int(pulseValue), dateTime_string])
        self.ids.pulseValue.text = ""

    def addNewTemperatureValue(self):
        temperatureValue = self.ids.temperatureValue.text
        print(temperatureValue)

        if temperatureValue is not '':
            with open('TemperatureData.csv', 'a', newline='') as csvFile:
                writer = csv.writer(csvFile, delimiter=';')
                now = datetime.now()
                dateTime_string = now.strftime("%d/%m/%Y %H:%M")
                writer.writerow([float(temperatureValue), dateTime_string])

        self.ids.temperatureValue.text = ""

    def addNewSaturationValue(self):
        saturationValue = self.ids.saturationValue.text
        print(saturationValue)

        if saturationValue is not '':
            with open('SaturationData.csv', 'a', newline='') as csvFile:
                writer = csv.writer(csvFile, delimiter=';')
                now = datetime.now()
                dateTime_string = now.strftime("%d/%m/%Y %H:%M")
                writer.writerow([int(saturationValue), dateTime_string])

        self.ids.saturationValue.text = ""

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
    _list_await = ['0']
    i = 0

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"

        self.sm = Builder.load_file("AppDesign.kv")
        return self.sm

    def func(self, msgTitle, msg):
        self._msgTitle = msgTitle
        self._msg = msg

    def saveForFileMessage(self):
        with open('Message.csv', 'a', newline='', encoding='utf-8') as csvFile:
            writer = csv.writer(csvFile, delimiter=';')
            writer.writerow([self._msgTitle, self._msg])

    def callback(self):
        self.notifier.notify( self._list_await[0],  self._list_await[1])
        for j in "li":
            self._list_await.pop(0)
            self.i = self.i - 1

        print("Wy??wietlono przypomnienie")
        # print("table await: ", self._list_await)

    def retDate(self, date, date_range):
        self._date = date
        self._date_range = date_range

    def save_time(self, instance, time):
        self._time = time
        print("time: ", str(time))
        self.saveForFileMessage()
        reminder = Reminder(str(time), self.callback)
        reminder.setReminders(self._date, self._date_range)
        self._list_await.insert(self.i, self._msgTitle)
        self._list_await.insert(self.i+1, self._msg)
        self.i = self.i + 2
        # print("table await: ", self._list_await)

    def cancel_time(self, instance, time):
        print("You clicked cancel!")

    def show_time_picker(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        time_dialog = MDTimePicker()
        time_dialog.bind(on_save=self.save_time, on_cancel=self.cancel_time)
        time_dialog.open()

    def save_date(self, instance, value, date_range):
        self.retDate(value, date_range)
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
