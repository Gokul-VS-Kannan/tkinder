from tkinter import *
root = Tk()
v = IntVar()
Radiobutton(root,text='GfG',variable=v,value=1).pack(anchor=W)
Radiobutton(root,text='MIT',variable=v,value=2).pack(anchor=W)
Radiobutton(root,text='GIG',variable=v,value=3).pack(anchor=W)
Radiobutton(root,text='GWG',variable=v,value=4).pack(anchor=W)
mainloop()