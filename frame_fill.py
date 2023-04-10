from logging import root
from tkinter import *
root=Tk()

f=Frame(root,height=800,width=800,bg="red")
f.propagate(0)

b=Button(f,text="SUBMIT",height=5,width=10,bg="blue")
b.pack(fill=Y,padx=200,pady=200)

f.pack()
f.mainloop()
