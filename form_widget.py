import tkinter as tk
# creating main window 
root = tk.Tk()
# set the aize of window
root.geometry("400x300")
# set the title for window
root.title("Sample Form")
# create and pack labels and entries
label_username = tk.Label(root,text="UserName: ",width=30,bd=3,font=("Arial",16,"bold"),cursor="hand2",fg="red")
label_username.pack(pady=5)
entry_username = tk.Entry(root,width=30)
entry_username.pack(pady=5)

label_password = tk.Label(root,text="Password: ",width=30,bd=3, font=("Arial",16,"bold"),cursor="hand2",fg="red")
label_password.pack(pady=5)
entry_password = tk.Entry(root,width=30)
entry_password.pack(pady=5)

submit_button = tk.Button(root, text="Submit",)
submit_button.pack(pady=20)

root.mainloop()