from tkinter import *
ad=Tk()
k=0
ad.geometry("500x500")
l=Label(ad,text="Enter first number:")
l.grid(row=0,column=0)
l=Label(ad,text="Enter second number:")
l.grid(row=1,column=0)
a=Entry(ad)
a.grid(row=0,column=1)
a1=Entry(ad)
a1.grid(row=1,column=1)
b=Button(ad,text="Add",command=lambda:add(a.get(),a1.get()))
b.grid(row=3,column=2)
def add(x,y):
    x=int(x)
    y=int(y)
    k=x+y
    l3=Label(ad,text="Result:")
    l3.grid(row=4,column=1)
    l2=Label(ad,text=k)
    l2.grid(row=4,column=2)
ad.mainloop() 
