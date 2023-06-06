from tkinter import *

def order_interface():
    # main home window
    orderWindow = Tk()
    orderWindow.title('')
    orderWindow.geometry('1450x800+10+10')
    orderWindow.config(bg='white')
    orderWindow.resizable(False, False)

    header_frame = Frame(orderWindow, width=1450, height=75, bg="#42758e")
    header_frame.place(x=0, y=0)

    main_heading = Label(orderWindow, text='Order Sheet', font='Verdana 40', bg='#42758e', fg='white')
    main_heading.pack(pady=10)

    icon_frame = Frame(orderWindow, width=140, height=705, bg="#42758e")
    icon_frame.place(x=10, y=85)

    imgHome = PhotoImage(file='homewhite.png').subsample(6)
    homeButton = Button(icon_frame, image=imgHome, bg='#42758e', bd=0, highlightthickness=0)
    homeButton.place(x=30, y=80)

    imgData = PhotoImage(file='databasewhite.png').subsample(6)
    databaseButton = Button(icon_frame, image=imgData, bg='#42758e', bd=0, highlightthickness=0)
    databaseButton.place(x=30, y=210)

    imgOrder = PhotoImage(file='orderblue.png').subsample(6)
    databaseButton = Button(icon_frame, image=imgOrder, bg='#42758e', bd=0, highlightthickness=0)
    databaseButton.place(x=30, y=340)

    imgHistory = PhotoImage(file='historywhite.png').subsample(6)
    databaseButton = Button(icon_frame, image=imgHistory, bg='#42758e', bd=0, highlightthickness=0)
    databaseButton.place(x=30, y=470)

    orderWindow.mainloop()

order_interface()