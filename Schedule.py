import time
import schedule


class MySchedule:

    _active = True

    def setReminder(self, time, action):
        conditionalAction = lambda action, self: action() if self._active else False
        # schedule.every().day.at(time).do(conditionalAction)
        conditionalAction(action, self)

    def activate(self):
        self._active = True

    def deactivate(self):
        self._active = False

mySchedule = MySchedule()
mySchedule.setReminder("01:13", lambda: print("test"))

while True:
    schedule.run_pending()
    time.sleep(1)
