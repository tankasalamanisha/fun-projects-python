from tkinter import *
import calendar
import sys

def generate_calendar(year):
    text = calendar.calendar(year)

    root = Tk()
    root.geometry("625x750")
    root.title(f"Calendar Year {year}")
    label1 = Label(root, text=f"Calendar Year {year}", bg= 'dark gray', font=("times",28, "bold"))
    label1.grid(row=1, column=1)
    root.config(background="white")
    l1 = Label(root,text=text, font="consolas 10")
    l1.grid(row=2, column=1, padx=20)
    root.mainloop()

if __name__ == "__main__":
    year= int(sys.argv[1])
    generate_calendar(year=year)