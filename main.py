import time
import schedule

from MyApp import MyApp, DateAndTimePicker
import _thread

from Notifier import Notifier


def print_time( threadName, delay):
   while True:
      time.sleep(delay)
      schedule.run_pending()

class Main(object):

    _thread.start_new_thread(print_time, ("Thread-1", 1,))

    myApp = MyApp()
    myApp.build()

    print("dupa2")

    notifier = Notifier()

    myApp.run()
    DateAndTimePicker().run()

    print("dupa3")
