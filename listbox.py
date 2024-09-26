from tkinter import *

top = Tk()
lb = Listbox(top)
lb.insert(1,'C++')
lb.insert(2,'C#')
lb.insert(3,'Java')
lb.insert(4,'Ruby')
lb.insert(5,'Python')
lb.insert(6,'JavaScript')
lb.pack()
top.mainloop()