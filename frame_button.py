from tkinter import * 
root=Tk()
f=Frame(root,height=800,width=800,bg="red",cursor="cross")
f.propagate(0)

b1=Button(f,text="Submit",height=5,width=15,bg="blue")
b1.pack()

b2=Button(f,text="Cancle",height=2,width=10,bg="green")
b2.pack()

def submit_button(s):
    print("Work has been submited !")
def cancle_button(s):
    print("process has been cancelled !")

b1.bind("<Button-1>",submit_button)
b2.bind("<Button-1>",cancle_button)

f.pack()
f.mainloop()