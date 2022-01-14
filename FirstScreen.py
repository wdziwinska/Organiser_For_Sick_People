from tkinter import *

from tkinter import *
from tkcalendar import *

class FirstScreen:
    pass

root = Tk()
root.geometry("600x500")
root['bg']='black'

def myClick():
    myLabel = Label(root, text="Look! I clicked")
    myLabel.pack()

def calendar():
    root = Tk()
    root.title('Kalendarz')
    # root.iconbitmap
    root.geometry("600x500")
    root['bg'] = 'black'

    cal = Calendar(root, selectmode="day", year=2022, month=1, day=17)
    cal.pack(pady=20, fill="both", expand=True)

    def grab_date():
        my_label.config(text="" + cal.get_date())
        selectedDate = cal.get_date()

    my_button = Button(root, text="Get Date", command=grab_date, fg = "white", bg="blue")
    my_button.pack(pady=20)

    my_label = Label(root, text="", fg = "white", bg="black")
    my_label.pack(pady=20)

    root.mainloop()

ustawPrzypomnienie = Button(root, text="Ustaw przypomnienie", command=calendar, fg = "white", bg="blue")
ustawPrzypomnienie.place(x=25, y=25)
ustawPrzypomnienie.pack()

kalendarz = Button(root, text="Kalendarz", command=myClick, fg = "white", bg="blue")
kalendarz.bind("<ButtonPress>", calendar)
kalendarz.place(x=30, y=60)
kalendarz.pack()

root.mainloop()