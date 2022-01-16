import time
import schedule

from MyGUI import MyGUI
import _thread


def print_time( threadName, delay):
   while True:
      time.sleep(delay)
      schedule.run_pending()

class Main(object):

    _thread.start_new_thread(print_time, ("Thread-1", 1,))

    myGUI = MyGUI()
    myGUI.build()

    print("dupa2")


    myGUI.run()
    print("dupa3")
