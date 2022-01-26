import asyncio
import threading
import time as t
from asyncio import Event
from datetime import datetime, timedelta
from time import sleep


from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.list import TwoLineListItem, OneLineListItem
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
        print(id(myGUI))

        messageTitle = self.ids.msgTitle.text
        message = self.ids.msg.text
        myGUI.func(messageTitle, message)
        print("AddMessaheWindows: tit and mess: ", messageTitle, message)


class MainWindow(Screen):
    def generateListOfMessage(self):
        listWindow = ListWindow()
        listWindow.messageForList()


class ListWindow(Screen):
    _iterator = iterator
    def messageForList(self):
        print("Iterator: ", self._iterator)
        if self._iterator < 1:
            csvFile = ReadCsvFile()
            messageTitleTable, messageTable, counter = csvFile.readFromFileMessage()
            print("List window: MesTit and mess: ", messageTitleTable, messageTable)
            for i in range(counter):
                self.ids.item.add_widget(TwoLineListItem(text=messageTitleTable[i], secondary_text=messageTable[i], on_release=self.release))
        self._iterator = self._iterator + 1

    def release(self, onelinelistitem):
        self.ids.item.remove_widget(onelinelistitem)

        updatedlist = []
        with open("Message.csv", newline="") as f:
            reader = csv.reader(f)
            clicked = onelinelistitem.text +";"+onelinelistitem.secondary_text

            for row in reader:
                if row[0] != clicked:
                    updatedlist.append(row)
            print(updatedlist)
            self.updatefile(updatedlist)

    def updatefile(self, updatedlist):
        with open("Message.csv", "w", newline="") as f:
            Writer = csv.writer(f)
            Writer.writerows(updatedlist)
            print("File has been updated")


class AddDataWindow(Screen):
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

    def addNewSaturationValue(self):
        saturationValue = self.ids.saturationValue.text
        print(saturationValue)

        if saturationValue is not '':
            with open('SaturationData.csv', 'a', newline='') as csvFile:
                writer = csv.writer(csvFile, delimiter=';')
                now = datetime.now()
                dateTime_string = now.strftime("%d/%m/%Y %H:%M")
                writer.writerow([int(saturationValue), dateTime_string])


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

    def saveForFileMessage(self):
        with open('Message.csv', 'a', newline='') as csvFile:
            writer = csv.writer(csvFile, delimiter=';')
            print("saveForFile: ", self._msgTitle, self._msg)
            writer.writerow([self._msgTitle, self._msg])

    def callback(self):
        print("messageTitle and message: ", self._msgTitle, self._msg)
        self.notifier.notify(self._msgTitle, self._msg)

    def retDate(self, date, date_range):
        self._date = date
        self._date_range = date_range
        print("date: ", str(self._date))
        print("date_range: ", str(self._date_range))

    def save_time(self, instance, time):
        reminder = Reminder(str(time), self.callback)

        print(str(time))
        currentDate = datetime.now()
        currentDateString = currentDate.strftime("%Y-%m-%d")


        if str(self._date_range) != '[]': #jezeli nie jest pusty (jezeli podano przedział dat)
            print("Relizuję przedział!")
            start_date_range = str(self._date_range[0])
            end_date_range = str(self._date_range[-1])

            day_int_start_date_range = int(start_date_range[8:10])
            day_int_end_date_range = int(end_date_range[8:10])
            day_int_currentDate = int(currentDateString[8:10])
            month_int_start = int(start_date_range[5:7])
            year_int_start = int(start_date_range[0:4])
            print("month: ", month_int_start)
            print("year: ", year_int_start)

            reminder.deactivate()

            if currentDateString == start_date_range or currentDateString == end_date_range:
                print("if")
                reminder.activate()
            elif day_int_start_date_range < day_int_currentDate < day_int_end_date_range:
                print("elif 1")
                day = day_int_start_date_range
                while day <= day_int_currentDate:
                    if day == day_int_currentDate:
                        reminder.activate()
                    day = day + 1
            elif day_int_currentDate < day_int_start_date_range:

                print("elif 2")
                sleep_until = start_date_range
                print("Czekam do dnia: ", sleep_until)
                reminder.deactivate()

                # # time.sleep(time.mktime(time.strptime(sleep_until, "%Y-%m-%d")))
                #
                # # tomorrow = datetime.replace(datetime.now() + timedelta(days=1),
                # #                                      hour=0, minute=0, second=0)
                # # delta = tomorrow - datetime.now()
                # # t.sleep(delta.seconds)
                #
                # # event = threading.Event()
                # # event.wait()
                #
                # await asyncio.sleep(60)
            else:
                print("daty przedziału różnią się od dzisiejszej daty")
                reminder.deactivate()

        else: #jeżeli podano jeden dzień (przedział jest pusty)
            print("Relizuję pojedynczy dzień!")
            if currentDateString != str(self._date):
                print("daty różnią się od siebie")
                reminder.deactivate()
            else:
                reminder.activate()

    def cancel_time(self, instance, time):
        print("You clicked cancel!")

    def show_time_picker(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        self.saveForFileMessage()
        time_dialog = MDTimePicker()
        time_dialog.bind(on_save=self.save_time, on_cancel=self.cancel_time)
        time_dialog.open()

    def save_date(self, instance, value, date_range):
        self.retDate(value, date_range)
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
