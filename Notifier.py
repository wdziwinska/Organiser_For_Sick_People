from plyer import notification


class Notifier:
    def notify(self, msgHeader, msg):
        notification.notify(
            title = msgHeader,
            message = msg,
            timeout = 100
        )