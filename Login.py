from tkinter import *
from tkinter import messagebox

def login_interface():
    # main login window
    login = Tk()
    login.title('')
    login.geometry('925x500+300+200')
    login.configure(bg="#FFF")
    login.resizable(False, False)

    # function to handle sign in button click
    def signin():
        username = user.get()
        password = code.get()

        # check if username and password match
        if username == "ritikagarg" and password == "candlecompany123":
            # destroy the window after successful login
            login.destroy()
            # user logs in after entering correct credentials

        else:
            # if the username and password do not match, display an error message
            messagebox.showerror('Invalid', "Invalid credentials. Please try again.")
            on_leave('e')

    # logo for the background
    img = PhotoImage(file='logowhite.png').subsample(3)
    # add the image to the main window
    Label(login, image=img, bg='white').place(x=40, y=140)

    # create a frame for the login form
    frame = Frame(login, width=350, height=350, bg="white")
    frame.place(x=480, y=70)

    # add a heading to the login form
    heading = Label(frame, text='Log in', fg='#42758e', bg='white', font='Verdana 23')
    heading.place(x=140, y=5)

    # function to clear the username entry when clicked on
    def on_enter(e):
        user.delete(0, 'end')

    # function to restore the default username if left empty
    def on_leave(e):
        name = user.get()
        if name == '':
            user.insert(0, 'Username')

    # add an entry field for the username
    user = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Ubuntu', 12), highlightthickness=0,
                 insertbackground="black")
    user.place(x=30, y=80)
    user.insert(0, "Username")
    # bind the on_enter and on_leave functions to the username entry
    user.bind('<FocusIn>', on_enter)
    user.bind('<FocusOut>', on_leave)

    # add a separator line between the username and password fields
    Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

    # function to clear the password entry when clicked on
    def on_enter(e):
        if code.get() == 'Password':
            code.delete(0, 'end')
            code.config(show='*')

    # function to restore the default password if left empty
    def on_leave(e):
        if code.get() == '':
            code.insert(0, 'Password')
            code.config(show='')

    # add an entry field for the password
    code = Entry(frame, width=25, fg='black', border=0, bg="white", font='Verdana 12', highlightthickness=0,
                 insertbackground='black')
    code.place(x=30, y=150)
    code.insert(0, "Password")
    # bind the on_enter and on_leave functions to the password entry
    code.bind('<FocusIn>', on_enter)
    code.bind('<FocusOut>', on_leave)

    # create a line separator using a frame widget
    Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

    # create a signin button
    Button(frame, width=25, pady=10, text='Log in', font='Verdana 14', bg='#0097b2', fg='black',
           bd=0, command=signin).place(x=45, y=230)

    # start the main loop for the GUI
    login.mainloop()

login_interface()