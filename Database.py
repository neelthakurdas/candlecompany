from tkinter import *
from tkinter import messagebox
from tkinter.constants import END
from tkinter import ttk
from tkcalendar import DateEntry
import openpyxl
from openpyxl import Workbook
import pathlib
import mysql.connector

def database_interface():
    # main tasks window
    dataWindow = Tk()
    dataWindow.title("Tasks")
    dataWindow.geometry('1100x700+175+100')
    dataWindow.config(bg='white')
    dataWindow.resizable(False, False)

    # heading for tasks interface
    heading = Label(dataWindow, text='Database', font='Verdana 70', bg='white', fg='#42758e')
    heading.pack(pady=10)

    # # images and buttons for respective app features
    # imgHome = PhotoImage(file="Gray_Images/Home_Gray.png").subsample(8)
    # homeButton = Button(dataWindow, image=imgHome, bg='white', bd=0, highlightthickness=0)
    # homeButton.place(x=50, y=150)
    #
    # imgTask = PhotoImage(file="Blue_Images/Tasks_Blue.png").subsample(8)
    # taskButton = Button(dataWindow, image=imgTask, bg='white', bd=0, highlightthickness=0)
    # taskButton.place(x=50, y=250)
    #
    # imgTime = PhotoImage(file="Gray_Images/Time_Gray.png").subsample(7)
    # timeButton = Button(dataWindow, image=imgTime, bg='white', bd=0, highlightthickness=0)
    # timeButton.place(x=50, y=350)
    #
    # imgGPA = PhotoImage(file="Gray_Images/GPA_Gray.png").subsample(6)
    # GPAButton = Button(dataWindow, image=imgGPA, bg='white', bd=0, highlightthickness=0, )
    # GPAButton.place(x=50, y=455)
    #
    # imgSettings = PhotoImage(file="Gray_Images/Set_Gray.png").subsample(8)
    # settingsButton = Button(dataWindow, image=imgSettings, bg='white', bd=0, highlightthickness=0)
    # settingsButton.place(x=50, y=560)

    # # callback functions: click button to go to a new page.
    # def homeClick():
    #     dataWindow.destroy()
    #     home_interface()
    #
    # homeButton.config(command=homeClick)
    #
    # def timeClick():
    #     dataWindow.destroy()
    #     timer_interface()
    #
    # timeButton.config(command=timeClick)
    #
    # def gpaClick():
    #     dataWindow.destroy()
    #     gpa_interface()
    #
    # GPAButton.config(command=gpaClick)
    #
    # def settingsClick():
    #     dataWindow.destroy()
    #     settings_interface()
    #
    # settingsButton.config(command=settingsClick)

    style = ttk.Style()

    # theme
    style.theme_use("default")
    style.configure("Treeview", background="white", foreground="black", rowheight=25, fieldbackground="white")

    # change selected color
    style.map("Treeview", background=[("selected", "darkred")])

    detail_frame = LabelFrame(dataWindow, text="Add Entry", font=("Ubuntu", 20), bg="lightgray", foreground="black",
                              relief=GROOVE)
    detail_frame.place(x=150, y=120, width=300, height=550)

    # data Frame
    data_frame = Frame(dataWindow, background="white", relief=GROOVE)
    data_frame.place(x=470, y=120, width=600, height=550)

    # task Label and Entry
    task_lab = Label(detail_frame, text="Item: ", font=("Ubuntu", 14), bg="lightgray", foreground="black")
    task_lab.place(x=10, y=16)

    task_ent = Entry(detail_frame, bd=1, font=("Ubuntu", 14), bg="white", foreground="black", highlightthickness=1)
    task_ent.place(x=90, y=17, width=200, height=30)

    # details Label and Entry
    details_lab = Label(detail_frame, text="ID: ", font=("Ubuntu", 14), bg="lightgray", foreground="black")
    details_lab.place(x=10, y=64)

    details_ent = Entry(detail_frame, bd=1, font=("Ubuntu", 14), bg="white", foreground="black", highlightthickness=1)
    details_ent.place(x=90, y=65, width=200, height=30)

    # location Label and Entry
    location_lab = Label(detail_frame, text="Price/Unit:", font=("Ubuntu", 14), bg="lightgray", foreground="black")
    location_lab.place(x=10, y=112)

    location_ent = Entry(detail_frame, bd=1, font=("Ubuntu", 14), bg="white", foreground="black", highlightthickness=1)
    location_ent.place(x=90, y=113, width=200, height=30)

    # start Date Label and Entry
    start_lab = Label(detail_frame, text="Date: ", font=("Ubuntu", 14), bg="lightgray", foreground="black")
    start_lab.place(x=10, y=160)

    start_ent = Entry(detail_frame, bd=1, font=("Ubuntu", 14), bg="white", foreground="black", highlightthickness=1)
    start_ent.place(x=90, y=161, width=200, height=30)

    # end Date Label and Entry
    end_lab = Label(detail_frame, text="End Date: ", font=("Ubuntu", 14), bg="lightgray", foreground="black")
    end_lab.place(x=10, y=208)

    end_ent = DateEntry(detail_frame, bd=1, font=("Ubuntu", 14), bg="white", foreground="black", highlightthickness=1)
    end_ent.place(x=90, y=209, width=200, height=30)

    # status Label and Entry
    status_lab = Label(detail_frame, text="Status: ", font=("Ubuntu", 14), bg="lightgray", foreground="black")
    status_lab.place(x=10, y=256)

    status_ent = ttk.Combobox(detail_frame, font=("Ubuntu", 14), background='white', foreground='black')
    status_ent["values"] = ("Yet to Start", "In Progress", "Completed")
    status_ent.place(x=90, y=257, width=200, height=30)

    # priority Label and Entry
    priority_lab = Label(detail_frame, text="Priority: ", font=("Ubuntu", 14), bg="lightgray", foreground="black")
    priority_lab.place(x=10, y=304)

    priority_ent = ttk.Combobox(detail_frame, font=("Ubuntu", 14), background='white', foreground='black')
    priority_ent["values"] = ("Very High", "High", "Medium", "Low", "Very Low")
    priority_ent.place(x=90, y=305, width=200, height=30)

    # database frame
    main_frame = Frame(data_frame, bg="white", bd=2, relief=GROOVE)
    main_frame.pack(fill=BOTH, expand=True)

    y_scroll = Scrollbar(main_frame, orient=VERTICAL)
    x_scroll = Scrollbar(main_frame, orient=HORIZONTAL)

    # treeview database
    table = ttk.Treeview(main_frame, columns=("Task", "Details", "Location", "Start Date", "End Date", "Status",
                                              "Priority"), yscrollcommand=y_scroll.set, xscrollcommand=x_scroll.set)

    # x-scrolls and y-scrolls
    y_scroll.config(command=table.yview)
    x_scroll.config(command=table.xview)

    y_scroll.pack(side=RIGHT, fill=Y)
    x_scroll.pack(side=BOTTOM, fill=X)

    # table headings
    table.heading("Task", text="Task")
    table.heading("Details", text="Details")
    table.heading("Location", text="Location")
    table.heading("Start Date", text="Start Date")
    table.heading("End Date", text="End Date")
    table.heading("Status", text="Status")
    table.heading("Priority", text="Priority")

    table["show"] = "headings"

    # set table column widths
    table.column("Task", width=100)
    table.column("Details", width=100)
    table.column("Location", width=100)
    table.column("Start Date", width=100)
    table.column("End Date", width=100)
    table.column("Status", width=100)
    table.column("Priority", width=100)

    table.pack(fill=BOTH, expand=True)

    data = []

    # creating odd and even rows
    global count
    count = 0
    for record in data:
        if count % 2 == 0:
            table.insert(parent="", index="end", text="", values=(
                record[0], record[1], record[2], record[3], record[4], record[5], record[6]), tags=("evenrow"))
        else:
            table.insert(parent="", index="end", text="", values=(
                record[0], record[1], record[2], record[3], record[4], record[5], record[6]), tags=("oddrow"))

        count += 1

    # functions that adds a record from data entries
    def add_record():
        # creating unique backgrounds and colours for odd-even rows
        table.tag_configure("oddrow", background="white", foreground='black')
        table.tag_configure("evenrow", background="#42758e", foreground='white')

        global count
        if count % 2 == 0:
            table.insert(parent="", index="end", iid=count, text="", values=(task_ent.get(), details_ent.get(),
                                                                             location_ent.get(), start_ent.get(),
                                                                             end_ent.get(), status_ent.get(),
                                                                             priority_ent.get(),), tags=("evenrow"))
        else:
            table.insert(parent="", index="end", iid=count, text="", values=(task_ent.get(), details_ent.get(),
                                                                             location_ent.get(), start_ent.get(),
                                                                             end_ent.get(), status_ent.get(),
                                                                             priority_ent.get(),), tags=("oddrow"))
        count += 1

    # function to delete record
    def delete_record():
        x = table.selection()
        table.delete(x)

    # function to clear an ongoing entry
    def clear_record():
        task_ent.delete(0, END)
        details_ent.delete(0, END)
        location_ent.delete(0, END)
        start_ent.delete(0, END)
        end_ent.delete(0, END)
        status_ent.delete(0, END)
        priority_ent.delete(0, END)

    # function to update records
    def update_record():
        selected = table.focus()
        table.item(selected, text="", values=(
            task_ent.get(), details_ent.get(), location_ent.get(), start_ent.get(), end_ent.get(), status_ent.get(),
            priority_ent.get()))

        task_ent.delete(0, END)
        details_ent.delete(0, END)
        location_ent.delete(0, END)
        start_ent.delete(0, END)
        end_ent.delete(0, END)
        status_ent.delete(0, END)
        priority_ent.delete(0, END)

        # clear boxes
        task_ent.delete(0, END),
        details_ent.delete(0, END),
        location_ent.delete(0, END),
        start_ent.delete(0, END),
        end_ent.delete(0, END)
        status_ent.delete(0, END),
        priority_ent.delete(0, END)

    # add Button
    add_btn = Button(detail_frame, bg="black", foreground="black", text="Add", bd=0, pady=7, highlightthickness=1,
                     font=("Ubuntu", 13), width=10, command=add_record)
    add_btn.place(x=22, y=425)

    # update Button
    update_btn = Button(detail_frame, bg="white", foreground="black", text="Update", bd=0, pady=7, highlightthickness=1,
                        font=("Ubuntu", 13), width=10, command=update_record)
    update_btn.place(x=152, y=425)

    # clear Button
    clear_btn = Button(detail_frame, bg="white", foreground="black", text="Clear", bd=0, pady=7, highlightthickness=1,
                       font=("Ubuntu", 13), width=10, command=clear_record)
    clear_btn.place(x=22, y=470)

    # delete Button
    delete_btn = Button(detail_frame, foreground="black", text="Delete", bd=0, pady=7, font=("Ubuntu", 13), width=10,
                        highlightthickness=1, command=delete_record)
    delete_btn.place(x=152, y=470)

    # function to save the current records
    def save():
        # define the path to the Excel file to be used or created
        file_path = pathlib.Path('data.xlsx')

        # check if the file exists, and if so, attempt to load it with openpyxl
        if file_path.exists():
            try:
                file = openpyxl.load_workbook(file_path)
            except Exception as e:
                # if the file cannot be loaded, display an error message and return
                messagebox.showerror('Error', f'Failed to load Excel file: {str(e)}')
                return
        else:
            # if the file does not exist, create a new workbook with the necessary columns
            file = Workbook()
            sheet = file.active
            sheet['A1'] = "Task"
            sheet['B1'] = "Details"
            sheet['C1'] = "Location"
            sheet['D1'] = "Start Date"
            sheet['E1'] = "End Date"
            sheet['F1'] = "Status"
            sheet['G1'] = "Priority"

        # get the data from the table widget and append it to the Excel sheet
        sheet = file.active
        for record in table.get_children():
            task = table.item(record)['values'][0]
            details = table.item(record)['values'][1]
            location = table.item(record)['values'][2]
            start_date = table.item(record)['values'][3]
            end_date = table.item(record)['values'][4]
            status = table.item(record)['values'][5]
            priority = table.item(record)['values'][6]
            sheet.append([task, details, location, start_date, end_date, status, priority])

        # attempt to save the Excel file and display an error message if saving fails
        try:
            file.save(file_path)
            file.close()
        except Exception as e:
            messagebox.showerror('Error', f'Failed to save Excel file: {str(e)}')
            return

        # clear the table widget and display a success message
        for record in table.get_children():
            table.delete(record)
        messagebox.showinfo('Info', 'Successfully saved!')

    # save button
    save_button = Button(dataWindow, text="Add to Cart", command=save, background="white", fg="black",
                         pady=7, width=8, highlightthickness=1, bd=0)
    save_button.place(x=965, y=70)

    # starts the event loop for the tasks window GUI
    dataWindow.mainloop()

database_interface()