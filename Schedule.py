import time
import schedule


class MySchedule:

    def setReminder(self, time, action):
        schedule.every().day.at(time).do(action)


# mySchedule = MySchedule()
# mySchedule.setReminder("00:42", lambda: print("dupa"))
#
# while True:
#     schedule.run_pending()
#     time.sleep(1)
