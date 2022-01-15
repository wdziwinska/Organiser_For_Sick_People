import time
import schedule


class Reminder:

    _active = True

    def __init__(self, time, action):
        def callback():
            if self._active:
                action()

        schedule.every().day.at(time).do(callback)

    def activate(self):
        self._active = True

    def deactivate(self):
        self._active = False

reminder = Reminder("02:00", lambda: print("test"))
# mySchedule.deactivate()

while True:
    schedule.run_pending()
    time.sleep(1)
