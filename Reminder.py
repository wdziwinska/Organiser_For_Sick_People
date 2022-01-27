import asyncio
import time
from datetime import datetime
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

    def setReminders(self, date, date_range):
        # print(str(time))
        currentDate = datetime.now()
        currentDateString = currentDate.strftime("%Y-%m-%d")

        if str(date_range) != '[]':  # jezeli nie jest pusty (jezeli podano przedział dat)
            print("Relizuję przedział!")
            start_date_range = str(date_range[0])
            end_date_range = str(date_range[-1])

            day_int_start_date_range = int(start_date_range[8:10])
            day_int_end_date_range = int(end_date_range[8:10])
            day_int_currentDate = int(currentDateString[8:10])
            month_int_start = int(start_date_range[5:7])
            # month_int_currentDate = int(currentDateString[5:7])
            year_int_start = int(start_date_range[0:4])
            print("month: ", month_int_start)
            print("year: ", year_int_start)

            self.deactivate()

            if currentDateString == start_date_range or currentDateString == end_date_range:
                print("if")
                self.activate()
            elif day_int_start_date_range < day_int_currentDate < day_int_end_date_range:
                print("elif 1")
                day = day_int_start_date_range
                while day <= day_int_currentDate:
                    if day == day_int_currentDate:
                        self.activate()
                    day = day + 1
            elif day_int_currentDate < day_int_start_date_range:

                print("elif 2")
                sleep_until = start_date_range
                print("Czekam do dnia: ", sleep_until)
                self.deactivate()
                # await asyncio.sleep(time.mktime(time.strptime(sleep_until, "%Y-%m-%d")))

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
                self.deactivate()

        else:  # jeżeli podano jeden dzień (przedział jest pusty)
            print("Relizuję pojedynczy dzień!")
            if currentDateString != str(date):
                print("daty różnią się od siebie")
                self.deactivate()
            else:
                self.activate()