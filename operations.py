from tkinter import filedialog, messagebox
import pandas as pd
import customtkinter as ctk
from PIL import ImageTk, Image
from tkinter import ttk
from customtkinter import *

df = pd.DataFrame()


import tkinter as tk
import sys
class Terminal(tk.Text):
    def __init__(self, master, *args, **kwargs):
        tk.Text.__init__(self, master, *args, **kwargs)
        self.pack(fill=tk.BOTH, expand=True)
        self.config(state=tk.DISABLED, bg='black', fg='white')
        sys.stdout = self

    def write(self, message):
        self.config(state=tk.NORMAL)
        self.insert(tk.END, message)
        self.see(tk.END)
        self.config(state=tk.DISABLED)
def start_terminal():
    root = CTk()
    root.title("Terminal")
    x_offset = 350  # Distance from the left edge of the screen
    y_offset = (1650 - root.winfo_reqheight()) // 2  # Center vertically

    # Set the window position
    root.geometry(f'400x200+{x_offset}+{y_offset}')

    terminal = Terminal(root)
    root.mainloop()



    # splitbox = CTk()
    # splitbox.title('Split Sheet')
    #
    # selected_col = tk.StringVar()
    #
    # frame = CTkFrame(splitbox)
    # label = CTkLabel(frame, text='Select Column ->').pack(side='left', padx=50, pady=5)
    # dropdown1 = CTkOptionMenu(frame, variable=selected_col, values=get_col()).pack(padx=50, pady=20)
    # frame.pack(pady=10)
    #
    # label1 = CTkLabel(splitbox, text='Add items on the behalf you want to split the Table').pack(padx=50, pady=5)
    # textstr = tk.StringVar()  # This variable should hold the input text
    # # GUI setup for entry field
    # getlist_entry = CTkEntry(splitbox, textvariable=textstr,
    #                          placeholder_text='Enter each Item separated by comma ( , ).', width=400).pack(padx=50,
    #                                                                                                        pady=5)
    # # Button setup to trigger the split_sheet function with selected column and entered text
    # btn = CTkButton(splitbox, text='Split', command='').pack(padx=50, pady=(5, 20))
    #
    # splitbox.mainloop()














def import_file():
    global df
    file_path: str = filedialog.askopenfilename(initialdir="Downloads\\covid", title="Select file",
                                                filetypes=(("CSV files", "*.csv"), ("Excel files", "*.xlsx;*.xls"),
                                                           ("All files", "*.*")))
    try:
        if file_path.endswith('.csv'):
            df = pd.read_csv(file_path)
            print('import')
            print(df.head())
        elif file_path.endswith('.xlsx') or file_path.endswith('.xls'):
            try:  # Read Excel file with openpyxl engine
                df = pd.read_excel(file_path, engine='openpyxl', sheet_name="Sheet1")
            except Exception as e_openpyxl:
                print("Error with openpyxl engine:", e_openpyxl)
                try:  # If reading with openpyxl fails, try xlrd engine
                    df = pd.read_excel(file_path, engine='xlrd', sheet_name="Sheet1")
                except Exception as e_xlrd:
                    print("Error with xlrd engine:", e_xlrd)
                    raise e_xlrd  # ----->  Raise the xlrd error if both engines fail
    except Exception as e:
        print("Error:", e)
        return None
    # create_table_widget(screen)
def get_col():
    global df
    column_list = [a for a in df.head()]
    return column_list



def save_dataframe():
    global df
    if df.empty:
        messagebox.showinfo('Info', 'Load Data first')
    else:
        filename = filedialog.asksaveasfilename(defaultextension=".csv",
                                                filetypes=[("CSV files", "*.csv"),
                                                           ("Excel files", "*.xlsx;*.xls"),
                                                           ("All files", "*.*")])
        if filename:
            if filename.endswith('.csv'):
                df.to_csv(filename, index=False)
                print("DataFrame saved as CSV to:", filename)
            elif filename.endswith('.xlsx') or filename.endswith('.xls'):
                df.to_excel(filename, index=False)
                print("DataFrame saved as Excel to:", filename)
def remove_file():
    global df
    if df.empty:
        messagebox.showinfo('Info', 'Load Data first')
    else:
        confirmation = messagebox.askquestion("Remove Data",
                                              f"Do you want to Remove the current data from the table?")
        if confirmation == 'yes':
            df = pd.DataFrame()
            print(df)
        else:
            print('No changes into Table')
    # create_table_widget(screen)
# below function the parameter is not global df--------------<Keep In Mind>
def store_data_info(df):
    data_info = {}
    for column in df.columns:
        unique_values = df[column].nunique()
        total_count = len(df[column])
        data_type = df[column].dtype
        null_values = df[column].isnull().sum()
        data_info[column] = {
            "col_dataType": data_type,
            "Unique values": unique_values,
            "Total values": total_count,
            "Null values": null_values
        }

    return pd.DataFrame(data_info)
def display_dataframe_info(df):
    root = CTk()
    root.title('DataFrame Information')
    x_offset = 1200  # Distance from the left edge of the screen
    y_offset = (650 - root.winfo_reqheight()) // 2  # Center vertically

    # Set the window position
    root.geometry(f'{x_offset}+{y_offset}')

    info_frame = CTkFrame(root, border_width=2)
    info_frame.pack(pady=10, padx=20, fill="both", expand=True)

    # Headings for the information
    headings = ["Column Name", "Data Type", "Unique Values", "Total Values", "Null Values"]
    for j, heading in enumerate(headings):
        CTkLabel(info_frame, text=heading, font=("Helvetica", 10, "bold")).grid(row=0, column=j, padx=10, pady=2, sticky=tk.W)

    for i, (column, info) in enumerate(df.items(), start=1):
        CTkLabel(info_frame, text=f"{column}").grid(row=i, column=0, padx=10, pady=2, sticky=tk.W)
        for j, (key, value) in enumerate(info.items(), start=1):
            CTkLabel(info_frame, text=f"{value}").grid(row=i, column=j, padx=10, pady=2, sticky=tk.W)

    root.mainloop()
def on_info():
    if df.empty:
        messagebox.showinfo('Info', 'Load Data first')
    else:
        display_dataframe_info(store_data_info(df))  # ----->  Here df is global
def del_col(col_name):
    confirmation = messagebox.askquestion("Delete Column",
                                          f"Do you want to delete the column '{col_name}' from the table?")
    if confirmation == 'yes':
        # Perform the deletion operation here
        df.drop(columns=[col_name], inplace=True)
        print(df)
        messagebox.showinfo('DONE', f'Column {col_name} Deleted successfully.')
    else:
        print("Deletion operation canceled.")

def del_nan(selected_col):
    global df
    print(selected_col)
    if selected_col != 'All Columns':
        df = df.dropna(subset=[selected_col])
        print(df)
    else:
        df = df.dropna()
def replace_nan(column, value):
    print(column)
    if column != 'All Columns':
        df[column].fillna(value, inplace=True)
        print(df)
    else:
        df.fillna(value, inplace=True)
def remove_duplicate(column):
    print(column)
    if column != 'All Columns':
        df.drop_duplicates(subset=[column], inplace=True)
    else:
        df.drop_duplicates(inplace=True)  # Apply changes to df inplace
        print(df)
    return df  # Return the modified DataFrame7
def configure_table_style():
    style = ttk.Style()
    style.configure("Treeview.Heading", font=('Helvetica', 10, 'bold'), foreground="black")
    style.configure("Treeview", font=('Helvetica', 10), foreground="black", rowheight=25)

def find(search_text):
    query = search_text  # Get the search query from the entry widget
    if query:  # Check if the query is not empty
        # Filter the DataFrame based on the query
        filtered_df = df[df.apply(lambda row: row.astype(str).str.contains(query, case=False).any(), axis=1)]
        # Clear the table
        table.delete(*table.get_children())
        # Insert filtered data into the table
        for index, row in filtered_df.iterrows():
            table.insert('', 'end', values=tuple(row))


def create_table_widget():
    print('Table View Activate')
    global tableView, show_table
    try:
        show_table.destroy()
    except NameError:
        pass
    def copy_selected():
        selected_data = []
        columns = None
        for item in table.selection():
            values = table.item(item)['values']
            if columns is None:
                # Retrieve column names for the first selected item
                columns = [table.heading(column)['text'] for column in table['columns']]
            # Create a dictionary with column names as keys and row values as values
            row_data = {column: value for column, value in zip(columns, values)}
            selected_data.append(row_data)
        # Create a DataFrame from the selected data
        copy_df = pd.DataFrame(selected_data)
        # Copy the DataFrame data to the clipboard in Excel-friendly format
        copy_df.to_clipboard(index=False, excel=True)
        print('Data copy Successfully')
        print(copy_df)
    # Close the clipboard window
    def edit_selected(event):
        selection = table.selection()
        if selection:
            # Get the values of the selected row
            values = table.item(selection[0])['values']
            # You can implement the editing functionality here
            print("Edit:", values)
    def delete_selected():
        selection = table.selection()
        if selection:
            if messagebox.askyesno("Delete", "Are you sure you want to delete the selected row(s)?"):
                for item in selection:
                    # Delete the corresponding row from the DataFrame
                    index = int(table.index(item))
                    df.drop(df.index[index], inplace=True)
                    # Delete the row from the table
                    table.delete(item)
            else:
                print('No Changes')

    configure_table_style()

    # Your existing logic for creating the Treeview widget and populating it with data
    show_table = CTk()

    # show_table.geometry('600x500')
    x_offset = 350  # Distance from the left edge of the screen
    y_offset = (650 - show_table.winfo_reqheight()) // 2  # Center vertically

    # Set the window position
    show_table.geometry(f'800x450+{x_offset}+{y_offset}')

    tableView = ctk.CTkFrame(show_table, corner_radius=15)
    tableView.pack(fill='both', padx=10, pady=10)

    vscrollbar = ctk.CTkScrollbar(tableView, orientation='vertical')
    hscrollbar = ctk.CTkScrollbar(tableView, orientation='horizontal')
    vscrollbar.pack(side='right', fill='y')
    hscrollbar.pack(side='bottom', fill='x')

    global table
    table = ttk.Treeview(tableView, height=30, yscrollcommand=vscrollbar.set, xscrollcommand=hscrollbar.set)
    vscrollbar.configure(command=table.yview)
    hscrollbar.configure(command=table.xview)

    table['columns'] = list(df.columns)
    table['show'] = 'headings'

    table.pack(expand=True, fill='both')

    for column in table['columns']:
        table.heading(column, text=column)

    for i, row in enumerate(df.values):
        if i % 2 == 0:
            table.insert('', 'end', values=tuple(row), tags=('even',))
        else:
            table.insert('', 'end', values=tuple(row), tags=('odd',))

    table.tag_configure('even', background='#838383')
    table.tag_configure('odd', background='#363636', foreground='#848484')

    # # Bindings
    table.bind('<Double-1>', edit_selected)  # Double click to edit
    show_table.bind('<Control-s>', lambda event: save_dataframe())  # Ctrl+S to save
    show_table.bind('<Delete>', lambda event: delete_selected())  # Delete key to delete
    show_table.bind('<Control-c>', lambda event: copy_selected())

    show_table.mainloop()



