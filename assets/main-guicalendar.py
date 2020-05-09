from tkinter import *
import calendar

def showCal():
    layarScreen1 = Tk()

    layarScreen1.config(background='white')
    layarScreen1.title('GUI CALENDAR')
    layarScreen1.geometry('550x600')

    fetch_year = int(year_field.get())
    cal_content = calendar.calendar(fetch_year)

    cal_year = Label(layarScreen1, text=cal_content, font='Consolas 10 bold')
    cal_year.grid(row=5, column=1, padx=20)

    layarScreen1.mainloop()

if __name__ == "__main__":
    layarScreen2 = Tk()

    layarScreen2.config(background='white')
    layarScreen2.title("CALENDAR")
    layarScreen2.geometry('250x140')

    cal = Label(layarScreen2, text='CALENDAR', bg='dark gray', font=('calibri', 30, 'bold'))
    cal.grid(row=1, column=1)

    year = Label(layarScreen2, text='Enter Year', bg='light green', font=('calibri', 10))
    year.grid(row=2, column=1)

    year_field = Entry(layarScreen2)
    year_field.grid(row=3, column=1)

    Show = Button(layarScreen2, text='Show Calendar', fg='Black', bg='Blue', font=('calibri', 10), command=showCal)
    Show.grid(row=4, column=1)
    
    Exit = Button(layarScreen2, text='Exit', fg='Black', bg='Red', font=('calibri', 10), command=exit)
    Exit.grid(row=6, column=1)

    layarScreen2.mainloop()