from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.picker import MDDatePicker

class Calendar(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        return Builder.load_file('CalendarDate.kv')

    def on_save(self, instance, value, date_range):
        # print(instance, value, date_range)
        self.root.ids.date_label.text = str(value)
        # self.root.ids.date_label.text = f'{str(date_range[0])} - {str(date_range[-1])}'

    def on_cancel(self, instance, value):
        self.root.ids.date_label.text = "You clicked cancel!"

    def show_date_picker(self):
        date_dialog = MDDatePicker(mode="range")
        date_dialog.bind(on_save=self.on_save, on_cancel = self.on_cancel)
        date_dialog.open()

Calendar().run()


#-------------------------
#Tkinter Calendar
#-------------------------
# from tkinter import *
# from tkcalendar import *
#
# root = Tk()
# root.title('Kalendarz')
# # root.iconbitmap
# root.geometry("600x500")
#
# cal = Calendar(root, selectmode="day", year=2022, month=1, day=17)
# cal.pack(pady=20, fill="both", expand=True)
#
# def grab_date():
#     my_label.config(text="" + cal.get_date())
#
#
# my_button = Button(root, text="Get Date", command = grab_date)
# my_button.pack(pady=20)
#
# my_label = Label(root, text="")
# my_label.pack(pady=20)
#
#
# root.mainloop()