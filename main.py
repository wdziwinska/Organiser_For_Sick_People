import time
import schedule

from MyApp import MyApp
import _thread


def print_time( threadName, delay):
   while True:
      time.sleep(delay)
      schedule.run_pending()

class Main(object):

    _thread.start_new_thread(print_time, ("Thread-1", 1,))

    myApp = MyApp()
    myApp.build()

    print("dupa2")


    myApp.run()
    print("dupa3")
