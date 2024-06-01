from tkinter import *
import re
from tkinter import filedialog
from tkinter import ttk, messagebox
import pandas as pd
# import tkinter as ctk
import sqlite3
# import psycopg2
# import cx_Oracle
# import pyodbc
# import mysql.connectord`
from PIL import ImageTk, Image
from customtkinter import *
from operations import *


def manage():
    def del_col_upd_list():
        del_col(selected_col.get())
        selected_col.set('')
        dropdown1.configure(values=get_col())

    def update_dropdown():
        if all_col.get():
            selected_col.set(value='All Columns')
            dropdown1.configure(state='disabled')
        elif not all_col.get():
            selected_col.set(value='')
            dropdown1.configure(state='active', values=get_col())

    def update_view():
        # Del_var on means del.Column
        if delete_var.get():
            selected_col.set(value='')
            checkbox.forget()
            delete_btn.grid_forget()
            replace_btn.grid_forget()
            replace_switch.configure(state='disabled')
            replace_var.set(False)
            label.grid_forget()
            entry.grid_forget()

            delete_btn_col.grid(pady=5)
        else:
            # Del_var off means del.NAN from the col.
            checkbox.pack(side='left', padx=5, pady=5)
            delete_btn.grid(pady=5)
            delete_btn_col.grid_forget()
            replace_switch.configure(state='active')
            if replace_var.get():
                delete_btn.grid_forget()
                label.grid(padx=10)
                entry.grid()
                replace_btn.grid(pady=5)
            else:
                replace_btn.grid_forget()
                label.grid_forget()
                entry.grid_forget()
                delete_btn.grid(pady=5)
        if duplicate_var.get():
            checkbox.pack(side='left', padx=5, pady=5)
            replace_btn.grid_forget()
            delete_btn_col.grid_forget()
            label.grid_forget()
            entry.grid_forget()
            delete_btn.grid_forget()
            replace_var.set(False)
            replace_switch.configure(state='disabled')
            delete_var.set(False)
            delete_switch.configure(state='disabled')
            remove_duplicate_btn.grid(pady=5)
        else:
            replace_switch.configure(state='active')
            delete_switch.configure(state='active')
            remove_duplicate_btn.grid_forget()

    if len(get_col()) == 0:
        messagebox.showinfo('Info', 'Load Data first')
    else:
        editbox = CTk()
        editbox.title('EditBox')
        # editbox.geometry('400x200')
        # Set the x and y offsets to position the window on the left side of the screen
        x_offset = 780  # Distance from the left edge of the screen
        y_offset = (1650 - editbox.winfo_reqheight()) // 2  # Center vertically

        # Set the window position
        editbox.geometry(f'{x_offset}+{y_offset}')
        # --> Variable Uses
        selected_col = StringVar()
        replace_var = BooleanVar()
        delete_var = BooleanVar()
        replace_value = StringVar()
        all_col = BooleanVar()
        duplicate_var = BooleanVar()
        # ------> Column Dropdown

        frame0 = CTkFrame(editbox, fg_color='transparent')
        frame0.grid(row=0, column=0, padx=5, pady=5)

        dropdown1 = CTkOptionMenu(frame0, variable=selected_col, values=get_col())
        dropdown1.pack(side='left', padx=5, pady=5)
        checkbox = CTkCheckBox(frame0, text='All Columns', border_width=1, variable=all_col, onvalue=True, offvalue=False,
                               command=lambda: update_dropdown())
        checkbox.pack(side='left', padx=5, pady=5)

        frame = CTkFrame(editbox, fg_color='transparent')
        frame.grid(row=1, column=0, padx=5, pady=5)

        delete_switch = CTkSwitch(frame, text='Delete Column', variable=delete_var, onvalue=True, offvalue=False,
                                  command=update_view)
        delete_switch.pack(side='left', padx=3, pady=3)
        # -------> Replace Switch
        replace_switch = CTkSwitch(frame, text='Replace', variable=replace_var, onvalue=True, offvalue=False,
                                   command=update_view)
        replace_switch.pack(side='left', padx=3, pady=3)
        duplicate_switch = CTkSwitch(frame, text='Remove Duplicate', variable=duplicate_var, onvalue=True, offvalue=False,
                                   command=update_view)
        duplicate_switch.pack(side='left', padx=3, pady=3)

        # -------> Replace Label and Entry
        label = CTkLabel(editbox, text='Use replace only when its important, it may cause loss in data quality')
        entry = CTkEntry(editbox, placeholder_text='Replace Value', textvariable=replace_value)
        # --------> Delete and Replace Button
        delete_btn_col = CTkButton(editbox, text='Delete Column', command=lambda: del_col_upd_list())
        delete_btn = CTkButton(editbox, text='Remove NaN', command=lambda: del_nan(selected_col.get()))
        delete_btn.grid(pady=5)
        replace_btn = CTkButton(editbox, text='Replace', command=lambda: replace_nan(selected_col.get(),
                                                                                    replace_value.get()))
        remove_duplicate_btn = CTkButton(editbox, text='Remove', command=lambda: remove_duplicate(selected_col.get()))

        editbox.mainloop()


# ------------------------------------->  ToolBox
toolbox = CTk()
toolbox.title('ToolBox')
toolbox.geometry('110x320')
toolbox.resizable(False, False)

# Calculate the screen width and height
screen_width = toolbox.winfo_screenwidth()
screen_height = toolbox.winfo_screenheight()

# Set the x and y offsets to position the window on the left side of the screen
x_offset = 200  # Distance from the left edge of the screen
y_offset = (750 - toolbox.winfo_reqheight()) // 2  # Center vertically

# Set the window position
toolbox.geometry(f'110x370+{x_offset}+{y_offset}')
# Load/Resize Images -----> logo,add,edit,info,save,url,search
logo = Image.open('assets/logo.png')
logo = ImageTk.PhotoImage(logo)

add = Image.open('assets/add.png')
add = add.resize((30,30))
add = ImageTk.PhotoImage(add)

db = Image.open('assets/db.png')
db = db.resize((30,30))
db = ImageTk.PhotoImage(db)

refresh = Image.open('assets/refresh.png')
refresh = refresh.resize((30,30))
refresh = ImageTk.PhotoImage(refresh)

remove = Image.open('assets/remove.png')
remove = remove.resize((30,30))
remove = ImageTk.PhotoImage(remove)

url = Image.open('assets/url.png')
url = url.resize((30,30))
url = ImageTk.PhotoImage(url)

info = Image.open('assets/info.png')
info = info.resize((30,30))
info = ImageTk.PhotoImage(info)

edit = Image.open('assets/edit.png')
edit = edit.resize((30,30))
edit = ImageTk.PhotoImage(edit)

save = Image.open('assets/save.png')
save = save.resize((30,30))
save = ImageTk.PhotoImage(save)

search = Image.open('assets/search.png')
search = search.resize((30,30))
search = ImageTk.PhotoImage(search)

terminal = Image.open('assets/terminal.png')
terminal = terminal.resize((30,30))
terminal = ImageTk.PhotoImage(terminal)

table = Image.open('assets/table.png')
table = table.resize((30,30))
table = ImageTk.PhotoImage(table)

split = Image.open('assets/split.png')
split = split.resize((30,30))
split = ImageTk.PhotoImage(split)

logo = CTkLabel(toolbox, text='', image=logo)
logo.pack(pady=(5, 10))
# ---------------------------------->   Working Icons
frame = CTkFrame(toolbox, height=100)
frame.pack(padx=5,  pady=(5, 0))
# First row
add = CTkButton(frame, text='', image=add, corner_radius=0, fg_color='transparent', width=0, hover_color="#3B3B3B",
                command=lambda: import_file())
add.grid(row=0, column=0, padx=1, pady=1)

refresh = CTkButton(frame, text='', image=refresh, corner_radius=0, fg_color='transparent', width=0, hover_color="#3B3B3B")
refresh.grid(row=0, column=1, padx=1, pady=1)
# Second row
remove = CTkButton(frame, text='', image=remove, corner_radius=0, fg_color='transparent', width=0, hover_color="#3B3B3B",
                   command=lambda: remove_file())
remove.grid(row=1, column=0, padx=1, pady=1)

info = CTkButton(frame, text='', image=info, corner_radius=0, fg_color='transparent', width=0, hover_color="#3B3B3B",
                 command=lambda: on_info())
info.grid(row=1, column=1, padx=1, pady=1)
# Third Row
edit = CTkButton(frame, text='', image=edit, corner_radius=0, fg_color='transparent', width=0, hover_color="#3B3B3B",
                 command=manage)
edit.grid(row=2, column=0, padx=1, pady=1)
save = CTkButton(frame, text='', image=save, corner_radius=0, fg_color='transparent', width=0, hover_color="#3B3B3B",
                 command=save_dataframe)
save.grid(row=2, column=1, padx=1, pady=1)
# Fourth Row
split = CTkButton(frame, text='', image=split, corner_radius=0, fg_color='transparent', width=0, hover_color="#3B3B3B", command='')
split.grid(row=3, column=0, padx=1, pady=1)
terminal = CTkButton(frame, text='', image=terminal, corner_radius=0, fg_color='transparent', width=0, hover_color="#3B3B3B", command=lambda: start_terminal())
terminal.grid(row=3, column=1, padx=1, pady=1)
# ---------------------------------------->    Upcoming
label = CTkLabel(toolbox, text='Upcoming')
label.pack(pady=(5, 0))

testing_frame = CTkFrame(toolbox)
testing_frame.pack(padx=5,  pady=(5, 0))

url = CTkButton(testing_frame, text='', image=url, corner_radius=0, fg_color='transparent', width=0, hover_color="#3B3B3B")
url.grid(row=0, column=0, padx=1, pady=1)

db = CTkButton(testing_frame, text='', image=db, corner_radius=0, fg_color='transparent', width=0, hover_color="#3B3B3B")
db.grid(row=0, column=1, padx=1, pady=1)

table = CTkButton(testing_frame, text='', image=table, corner_radius=0, fg_color='transparent', width=0, hover_color="#3B3B3B",
                command=lambda: create_table_widget())
table.grid(row=1, column=0, padx=1, pady=1)

toolbox.mainloop()









