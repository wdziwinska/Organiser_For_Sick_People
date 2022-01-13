import schedule
import datetime
import time
from datetime import datetime, timedelta

class Schedule:

    # nowDateTime = datetime.now()
    # print(nowDateTime)
    # print(type(nowDateTime))
    #
    # nowTime = time.time()
    # print(nowTime)
    #
    # current_time = nowDateTime.strftime("%H:%M")
    # print("Current Time =", current_time)
    # schedule.every().day.at(current_time)

    def setTime(self):
        current_date_and_time = datetime.now()
        print(current_date_and_time)

        seconds = 15
        seconds_added = timedelta(seconds=seconds)
        future_date_and_time = current_date_and_time + seconds_added
        print(future_date_and_time)
