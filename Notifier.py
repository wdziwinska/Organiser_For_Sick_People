from plyer import notification


class Notifier:
    def getReminderAbMedicines(self):
        notification.notify(
            title = "Przypomnienie o lakach",
            message = "Weź leki",
            timeout = 100
        )