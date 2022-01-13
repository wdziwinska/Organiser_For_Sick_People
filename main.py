from kivy.lang import Builder

from Notifier import Notifier
from Schedule import Schedule
from MyApp import MyApp

from datetime import datetime, timedelta

class Main(object):
        notifier = Notifier()
        schedule = Schedule()
        myApp = MyApp()

        app1 = myApp.build()


        # app2 = myApp.button2()

        alarm = schedule.setTime()
        # while alarm != datetime.now():
        #         print("")
        print(alarm)
        notifier.getReminderAbMedicines()


#-------------------------------
#tkinter
# import tkinter
# import tkinter.messagebox
#
#
# root = tkinter.Tk()
# root.title("Organizer dla osoby chorej")
#
# listbox_task = tkinter.Listbox(root, height=20, width=50)
# listbox_task.pack()
#
# root.mainloop()

#---------------------------------
# #kivy
# from kivy.app import App
# from kivy.uix.widget import Widget
#
# class MainWidget(Widget):
#     pass
#
# class TheApp(App):
#     pass
#
# TheApp().run()

