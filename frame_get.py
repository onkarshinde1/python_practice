from struct import pack
from tkinter import * 
root=Tk() 
f=Frame(root,width=500,height=500,bg="pink") 
f.pack() 
def click(s): 
    x=v1.get() 
    y=v2.get() 
    z=v3.get() 
    a=v4.get() 
    b=v5.get() 
    str="You have selected following option\n:" 
    if x==1: 
        str+="PYTHON" 
    if y==1: 
        str+="JAVA" 
    if z==1: 
        str+="OS" 
    if a==1: 
        str+="MED" 
    if b==1: 
        str+="CN" 
       # print("You have selected Following method:",str) 
    l=Label(f,text=str,fg="green",bg="red") 
    l.place(x=100,y=250)
v1=IntVar() 
v2=IntVar() 
v3=IntVar() 
v4=IntVar() 
v5=IntVar() 
c=Checkbutton(f,text="PYTHON",Variable=v1) 
c.place(x=50,y=100) 
c1=Checkbutton(f,text="JAVA",Variable=v2) 
c1.place(x=200,y=100) 
c2=Checkbutton(f,text="OS",Variable=v3) 
c2.place(x=350,y=100) 
c3=Checkbutton(f,text="MED",Variable=v4) 
c3.place(x=450,y=100) 
c4=Checkbutton(f,text="CN",Variable=v5) 
c4.place(x=550,y=100) 
b=Button(f,text="SUBMIT") 
b.place(x=350,y=200) 
b.bind("<Button-1>",click) 

root.mainloop() 
#EVENT HANDLING