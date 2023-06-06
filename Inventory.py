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
    dataWindow.title('')
    dataWindow.geometry('1450x800+10+10')
    dataWindow.config(bg='white')
    dataWindow.resizable(False, False)

    #creating frames for the GUI
    header_frame = Frame(dataWindow, width=1450, height=75, bg="#42758e")
    header_frame.place(x=0, y=0)

    icon_frame = Frame(dataWindow, width=140, height=705, bg="#42758e")
    icon_frame.place(x=10, y=85)

    main_frame = Frame(dataWindow, width=960, height=705, bg="#42758e")
    main_frame.place(x=480, y=85)

    data_frame = Frame(main_frame, background="lightblue", relief=GROOVE)
    data_frame.place(x=20, y=100, width=920, height=590)

    search_frame = Frame(main_frame, background="lightblue", width=920, height=60, relief=GROOVE)
    search_frame.place(x=20, y=20)

    imgHome = PhotoImage(file='homewhite.png').subsample(6)
    homeButton = Button(icon_frame, image=imgHome, bg='#42758e', bd=0, highlightthickness=0)
    homeButton.place(x=30, y=80)

    imgData = PhotoImage(file='databaseblue.png').subsample(6)
    databaseButton = Button(icon_frame, image=imgData, bg='#42758e', bd=0, highlightthickness=0)
    databaseButton.place(x=30, y=210)

    imgOrder = PhotoImage(file='orderwhite.png').subsample(6)
    databaseButton = Button(icon_frame, image=imgOrder, bg='#42758e', bd=0, highlightthickness=0)
    databaseButton.place(x=30, y=340)

    imgHistory = PhotoImage(file='historywhite.png').subsample(6)
    databaseButton = Button(icon_frame, image=imgHistory, bg='#42758e', bd=0, highlightthickness=0)
    databaseButton.place(x=30, y=470)

    #heading
    main_heading = Label(dataWindow, text='Database', font='Verdana 40', bg='#42758e', fg='white')
    main_heading.pack(pady=10)

    style = ttk.Style()
    style.theme_use("default")
    style.configure("Treeview", background="white", foreground="black", rowheight=25, fieldbackground="white")
    style.map("Treeview", background=[("selected", "darkred")])

    def validate_float(value):
        if value == "":
            return True
        try:
            float(value)
            return True
        except ValueError:
            return False

    validate_cmd = dataWindow.register(validate_float)

#------------------------------------DETAIL FRAME---------------------------------------------------------

    detail_frame = LabelFrame(dataWindow, font='Verdana 20', bg="#42758e", foreground="black",
                              relief=GROOVE)
    detail_frame.place(x=170, y=85, width=290, height=705)

    detail_heading = Label(detail_frame, text='Manage Inventory', font='Verdana 20', bg='#42758e', fg='white')
    detail_heading.pack(pady=10)

    #Product ID
    id_lab = Label(detail_frame, text="ID", font="Verdana 13", bg="#42758e", foreground="white")
    id_lab.place(x=10, y=75)

    id_ent = Entry(detail_frame, bd=1, font="Verdana 13", bg="white", foreground="black", highlightthickness=1)
    id_ent.place(x=100, y=75, width=170, height=30)

    #Fragrance
    frag_lab = Label(detail_frame, text="Fragrance", font="Verdana 13", bg="#42758e", foreground="white")
    frag_lab.place(x=10, y=125)

    frag_ent = Entry(detail_frame, bd=1, font="Verdana 13", bg="white", foreground="black", highlightthickness=1)
    frag_ent.place(x=100, y=125, width=170, height=30)

    #Jar
    jar_lab = Label(detail_frame, text="Jar", font="Verdana 13", bg="#42758e", foreground="white")
    jar_lab.place(x=10, y=175)

    jar_ent = Entry(detail_frame, bd=1, font="Verdana 13", bg="white", foreground="black", highlightthickness=1)
    jar_ent.place(x=100, y=175, width=170, height=30)

    #Size
    size_lab = Label(detail_frame, text="Size", font="Verdana 13", bg="#42758e", foreground="white")
    size_lab.place(x=10, y=225)

    size_ent = Entry(detail_frame, bd=1, font="Verdana 13", bg="white", foreground="black", highlightthickness=1)
    size_ent.place(x=100, y=225, width=170, height=30)

    #Colour
    colour_lab = Label(detail_frame, text="Colour", font="Verdana 13", bg="#42758e", foreground="white")
    colour_lab.place(x=10, y=275)

    colour_ent = Entry(detail_frame, bd=1, font="Verdana 13", bg="white", foreground="black", highlightthickness=1)
    colour_ent.place(x=100, y=275, width=170, height=30)

    #Set
    set_lab = Label(detail_frame, text="Set", font="Verdana 13", bg="#42758e", foreground="white")
    set_lab.place(x=10, y=325)

    set_ent = Entry(detail_frame, bd=1, font="Verdana 13", bg="white", foreground="black", highlightthickness=1)
    set_ent.place(x=100, y=325, width=170, height=30)

    #Location
    location_lab = Label(detail_frame, text="Location", font="Verdana 13", bg="#42758e", foreground="white")
    location_lab.place(x=10, y=375)

    location_ent = Entry(detail_frame, bd=1, font="Verdana 13", bg="white", foreground="black", highlightthickness=1)
    location_ent.place(x=100, y=375, width=170, height=30)

    #Quantity
    quantity_lab = Label(detail_frame, text="Quantity", font="Verdana 13", bg="#42758e", foreground="white")
    quantity_lab.place(x=10, y=425)

    quantity_ent = Entry(detail_frame, bd=1, font="Verdana 13", bg="white", foreground="black", highlightthickness=1,
                         validate="key", validatecommand=(validate_cmd, "%P"))
    quantity_ent.place(x=100, y=425, width=170, height=30)

    #Cost
    cost_lab = Label(detail_frame, text="Cost", font="Verdana 13", bg="#42758e", foreground="white")
    cost_lab.place(x=10, y=475)

    cost_ent = Entry(detail_frame, bd=1, font="Verdana 13", bg="white", foreground="black", highlightthickness=1,
                     validate="key", validatecommand=(validate_cmd, "%P"))
    cost_ent.place(x=100, y=475, width=170, height=30)

    #Price
    price_lab = Label(detail_frame, text="Price", font="Verdana 13", bg="#42758e", foreground="white")
    price_lab.place(x=10, y=525)

    price_ent = Entry(detail_frame, bd=1, font="Verdana 13", bg="white", foreground="black", highlightthickness=1,
                      validate="key", validatecommand=(validate_cmd, "%P"))
    price_ent.place(x=100, y=525, width=170, height=30)

#---------------------------------------TABLE FRAME----------------------------------------------------------

    #data frame
    db_frame = Frame(data_frame, bg="white", bd=2, relief=RIDGE)
    db_frame.pack(fill=BOTH, expand=True)

    y_scroll = Scrollbar(db_frame, orient=VERTICAL)
    x_scroll = Scrollbar(db_frame, orient=HORIZONTAL)

    # treeview database
    table = ttk.Treeview(db_frame, columns=("ID", "Fragrance", "Jar", "Size", "Colour", "Set",
                                            "Location", "Quantity", "Cost", "Price", "Profit",
                                            "Total Cost", "Total Price", "Total Profit"),
                                            yscrollcommand=y_scroll.set, xscrollcommand=x_scroll.set)

    # x-scrolls and y-scrolls
    y_scroll.config(command=table.yview)
    x_scroll.config(command=table.xview)

    y_scroll.pack(side=RIGHT, fill=Y)
    x_scroll.pack(side=BOTTOM, fill=X)

    # table headings
    table.heading("ID", text="ID")
    table.heading("Fragrance", text="Fragrance")
    table.heading("Jar", text="Jar")
    table.heading("Size", text="Size")
    table.heading("Colour", text="Colour")
    table.heading("Set", text="Set")
    table.heading("Location", text="Location")
    table.heading("Quantity", text="Quantity")
    table.heading("Cost", text="Cost")
    table.heading("Price", text="Price")
    table.heading("Profit", text="Profit")
    table.heading("Total Cost", text="Total Cost")
    table.heading("Total Price", text="Total Price")
    table.heading("Total Profit", text="Total Profit")

    table["show"] = "headings"

    # set table column widths
    table.column("ID", width=120)
    table.column("Fragrance", width=120)
    table.column("Jar", width=120)
    table.column("Size", width=120)
    table.column("Colour", width=120)
    table.column("Set", width=120)
    table.column("Location", width=120)
    table.column("Quantity", width=120)
    table.column("Cost", width=120)
    table.column("Price", width=120)
    table.column("Profit", width=120)
    table.column("Total Cost", width=120)
    table.column("Total Price", width=120)
    table.column("Total Profit", width=120)

    table.pack(fill=BOTH, expand=True)

    data = []

    global count

    for record in data:
        table.insert(parent="", index="end", text="", values=(
                    record[0], record[1], record[2], record[3], record[4], record[5], record[6],
                    record[7], record[8], record[9], record[10], record[11], record[12], record[13]))

    def add():
        quantity = int(quantity_ent.get())
        cost = round(float(cost_ent.get()), 2)
        price = round(float(price_ent.get()), 2)

        profit = round(price - cost, 2)
        total_cost = round(quantity * cost, 2)
        total_price = round(quantity * price, 2)
        total_profit = round(quantity * profit, 2)

        table.insert(parent="", index="end", text="", values=(id_ent.get(), frag_ent.get(), jar_ent.get(),
                                                              size_ent.get(), colour_ent.get(), set_ent.get(),
                                                              location_ent.get(), quantity,
                                                              cost, price, profit, total_cost,
                                                              total_price, total_profit
                                                              ))

        id_ent.delete(0, END)
        frag_ent.delete(0, END)
        jar_ent.delete(0, END)
        size_ent.delete(0, END)
        colour_ent.delete(0, END)
        set_ent.delete(0, END)
        location_ent.delete(0, END)
        quantity_ent.delete(0, END)
        cost_ent.delete(0, END)
        price_ent.delete(0, END)

    def update():
        selected = table.focus()
        table.item(selected, text="", values=(id_ent.get(), frag_ent.get(), jar_ent.get(), size_ent.get(),
                                              colour_ent.get(), set_ent.get(), location_ent.get(), quantity_ent,
                                              cost_ent.get(), price_ent.get()))

        id_ent.delete(0, END)
        frag_ent.delete(0, END)
        jar_ent.delete(0, END)
        size_ent.delete(0, END)
        colour_ent.delete(0, END)
        set_ent.delete(0, END)
        location_ent.delete(0, END)
        quantity_ent.delete(0, END)
        cost_ent.delete(0, END)
        price_ent.delete(0, END)

    def clear():
        id_ent.delete(0, END)
        frag_ent.delete(0, END)
        jar_ent.delete(0, END)
        size_ent.delete(0, END)
        colour_ent.delete(0, END)
        set_ent.delete(0, END)
        location_ent.delete(0, END)
        quantity_ent.delete(0, END)
        cost_ent.delete(0, END)
        price_ent.delete(0, END)

    def delete():
        x = table.selection()
        table.delete(x)

# ----------------------------------SEARCH FRAME-----------------------------------------------------------

    combo_search_by = ttk.Combobox(search_frame, width=20, font="Verdana 15", state="readonly",
                                   )
    combo_search_by["values"] = (
    "ID", "Product ID.", "Product Type", "Model No", "Manufacturer", "Department", "Location", "Incharge")
    combo_search_by.current(0)
    combo_search_by.place(x=40, y=20)

    # add Button

    add_btn = Button(detail_frame, bg="black", foreground="black", text="Add", bd=0, pady=7, highlightthickness=1,
                     font="Verdana 13", width=10, command=add)
    add_btn.place(x=17, y=600)

    # update Button
    update_btn = Button(detail_frame, bg="white", foreground="black", text="Update", bd=0, pady=7, highlightthickness=1,
                        font="Verdana 13", width=10, command=update)
    update_btn.place(x=147, y=600)

    # clear Button
    clear_btn = Button(detail_frame, bg="white", foreground="black", text="Clear", bd=0, pady=7, highlightthickness=1,
                       font="Verdana 13", width=10, command=clear)
    clear_btn.place(x=17, y=645)

    # delete Button
    delete_btn = Button(detail_frame, foreground="black", text="Delete", bd=0, pady=7, font="Verdana 13", width=10,
                        highlightthickness=1, command=delete)
    delete_btn.place(x=147, y=645)

    dataWindow.mainloop()

database_interface()

