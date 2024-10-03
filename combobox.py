import tkinter as tk 
from tkinter import ttk

def on_select(event):
    selected_item = combo_box.get()
    label.config(text="Selected Item:"+selected_item)
root = tk.Tk()
root.title("Combobox Example")

#create label
label = tk.Label(root,text="Selected Item:")
label.pack(pady=10)

#create a combobox widget
combo_box = ttk.Combobox(root,values=["Option 1","Option 2","Option 3"])
combo_box.pack(pady=5)

#set default value
combo_box.set("Option 1")

#bind event to selection 
combo_box.bind("<<ComboboxSelected>>",on_select)
root.mainloop()