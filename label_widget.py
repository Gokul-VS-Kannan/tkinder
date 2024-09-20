import tkinter as tk 

#  create main window
root = tk.Tk()

# set the size of window
root.geometry("400x250")
# set window title
root.title("Welcome to my app")

# creating string variable associated with the label
text_var = tk.StringVar()
text_var.set("Hello Everyone")

# create lable widget with all options
label =tk.Label(root,textvariable=text_var,anchor=tk.CENTER,bg="lightblue",height=3,width=30,bd=3,font=("Arial",16,"bold"),cursor="hand2",fg="red",padx=15,justify=tk.CENTER,relief=tk.RAISED,underline=0,wraplength=250)


# pack the label into the window
label.pack(pady=20)  # add padding to the top 

# run the main event loop
root.mainloop()