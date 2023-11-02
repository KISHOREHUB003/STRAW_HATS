import tkinter as tk
import tkinter.messagebox as messagebox
import database_interaction as db

def display_table_data():
   result = db.get_table_data()
   text.delete(1.0, tk.END)
   text.insert(tk.END, result)

def display_column_data():
   column_name = column_entry.get()
   result = db.get_column_data(column_name)
   text.delete(1.0, tk.END)
   text.insert(tk.END, result)

def add_data():
   name = name_entry.get()
   phone = int(phone_entry.get())
   address = address_entry.get()
   db.add_data(name, phone, address)
   messagebox.showinfo("Data Update", "Data added successfully")

def edit_data():
   name = edit_name_entry.get()
   column_name = edit_column_entry.get()
   new_value = edit_value_entry.get()
   db.edit_data(name, column_name, new_value)
   messagebox.showinfo("Data Update", "Data edited successfully")

def delete_data():
   name = delete_name_entry.get()
   db.delete_data(name)
   messagebox.showinfo("Data Update", "Data deleted successfully")

def exit_program():
   root.destroy()

root = tk.Tk()
root.geometry("800x600")
root.title("Database Interaction Application")

# Display Table Data Section
display_table_frame = tk.Frame(root)
display_table_frame.grid(row=0, column=0, padx=10, pady=10)
display_table_btn = tk.Button(display_table_frame, text="Display Table Data", command=display_table_data)
display_table_btn.pack()

# Display Specific Column Section
display_column_frame = tk.Frame(root)
display_column_frame.grid(row=1, column=0, padx=10, pady=10)
column_label = tk.Label(display_column_frame, text="Enter Column Name:")
column_label.pack()
column_entry = tk.Entry(display_column_frame)
column_entry.pack()
display_column_btn = tk.Button(display_column_frame, text="Display Specific Column", command=display_column_data)
display_column_btn.pack()

# Add Data Section
add_data_frame = tk.Frame(root)
add_data_frame.grid(row=2, column=0, padx=10, pady=10)
name_label = tk.Label(add_data_frame, text="Name:")
name_label.grid(row=0, column=0, padx=5, pady=5)
name_entry = tk.Entry(add_data_frame)
name_entry.grid(row=0, column=1, padx=5, pady=5)
phone_label = tk.Label(add_data_frame, text="Phone:")
phone_label.grid(row=1, column=0, padx=5, pady=5)
phone_entry = tk.Entry(add_data_frame)
phone_entry.grid(row=1, column=1, padx=5, pady=5)
address_label = tk.Label(add_data_frame, text="Address:")
address_label.grid(row=2, column=0, padx=5, pady=5)
address_entry = tk.Entry(add_data_frame)
address_entry.grid(row=2, column=1, padx=5, pady=5)
add_data_btn = tk.Button(add_data_frame, text="Add Data", command=add_data)
add_data_btn.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Edit Data Section
edit_data_frame = tk.Frame(root)
edit_data_frame.grid(row=3, column=0, padx=10, pady=10)
edit_name_label = tk.Label(edit_data_frame, text="Name:")
edit_name_label.grid(row=0, column=0, padx=5, pady=5)
edit_name_entry = tk.Entry(edit_data_frame)
edit_name_entry.grid(row=0, column=1, padx=5, pady=5)
edit_column_label = tk.Label(edit_data_frame, text="Column to Edit:")
edit_column_label.grid(row=1, column=0, padx=5, pady=5)
edit_column_entry = tk.Entry(edit_data_frame)
edit_column_entry.grid(row=1, column=1, padx=5, pady=5)
edit_value_label = tk.Label(edit_data_frame, text="New Value:")
edit_value_label.grid(row=2, column=0, padx=5, pady=5)
edit_value_entry = tk.Entry(edit_data_frame)
edit_value_entry.grid(row=2, column=1, padx=5, pady=5)
edit_data_btn = tk.Button(edit_data_frame, text="Edit Data", command=edit_data)
edit_data_btn.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Delete Data Section
delete_data_frame = tk.Frame(root)
delete_data_frame.grid(row=4, column=0, padx=10, pady=10)
delete_name_label = tk.Label(delete_data_frame, text="Name:")
delete_name_label.pack()
delete_name_entry = tk.Entry(delete_data_frame)
delete_name_entry.pack()
delete_data_btn = tk.Button(delete_data_frame, text="Delete Data", command=delete_data)
delete_data_btn.pack()

# Exit Section
exit_frame = tk.Frame(root)
exit_frame.grid(row=5, column=0, padx=10, pady=10)
exit_btn = tk.Button(exit_frame, text="Exit", command=exit_program)
exit_btn.pack()

# Text Display Section
text_frame = tk.Frame(root)
text_frame.grid(row=0, column=1, rowspan=6, padx=10, pady=10)
text = tk.Text(text_frame, height=20, width=40)
text.pack()

root.mainloop()
