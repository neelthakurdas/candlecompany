from tkinter import *

def home_interface():
    # main home window
    homeWindow = Tk()
    homeWindow.title('')
    homeWindow.geometry('1450x800+10+10')
    homeWindow.config(bg='white')
    homeWindow.resizable(False, False)

    header_frame = Frame(homeWindow, width=1450, height=75, bg="#42758e")
    header_frame.place(x=0, y=0)

    main_heading = Label(homeWindow, text='Home', font='Verdana 40', bg='#42758e', fg='white')
    main_heading.pack(pady=10)

    icon_frame = Frame(homeWindow, width=140, height=705, bg="#42758e")
    icon_frame.place(x=10, y=85)

    imgHome = PhotoImage(file='homeblue.png').subsample(6)
    homeButton = Button(icon_frame, image=imgHome, bg='#42758e', bd=0, highlightthickness=0)
    homeButton.place(x=30, y=80)

    imgData = PhotoImage(file='databasewhite.png').subsample(6)
    databaseButton = Button(icon_frame, image=imgData, bg='#42758e', bd=0, highlightthickness=0)
    databaseButton.place(x=30, y=210)

    imgOrder = PhotoImage(file='orderwhite.png').subsample(6)
    databaseButton = Button(icon_frame, image=imgOrder, bg='#42758e', bd=0, highlightthickness=0)
    databaseButton.place(x=30, y=340)

    imgHistory = PhotoImage(file='historywhite.png').subsample(6)
    databaseButton = Button(icon_frame, image=imgHistory, bg='#42758e', bd=0, highlightthickness=0)
    databaseButton.place(x=30, y=470)

    homeWindow.mainloop()

home_interface()