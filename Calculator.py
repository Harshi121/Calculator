import tkinter
from tkinter import *

base=tkinter.Tk()

base.title("Calculator")


a=Entry(base,width=35, borderwidth=5)
a.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

def button_click(number):
    current=a.get()
    a.delete(0, END)
    a.insert(0,str(current) + str(number))

def button_clear():
    a.delete(0, END)

def button_add():
    first_num=a.get()
    global f_num
    global math
    math="Addition"
    f_num= int(first_num)
    a.delete(0, END)


def button_subtract():
    first_num=a.get()
    global f_num
    global math
    math="Subtraction"
    f_num= int(first_num)
    a.delete(0, END)

def button_multiply():
    first_num=a.get()
    global f_num
    global math
    math="Multiplication"
    f_num= int(first_num)
    a.delete(0, END)

def button_divide():
    first_num=a.get()
    global f_num
    global math
    math="Division"
    f_num= int(first_num)
    a.delete(0, END)
    
def button_equal():
    second_n=a.get()
    a.delete(0, END)
    if math=="Addition":
        a.insert(0, f_num + int(second_n))
    elif math=="Subtraction":
        a.insert(0, f_num - int(second_n))
    elif math=="Multiplication":
        a.insert(0, f_num * int(second_n))
    elif math=="Division":
        a.insert(0, f_num / int(second_n))

button_1=Button(base,text="1",padx=40,pady=20,command=lambda:button_click(1))
button_2=Button(base,text="2",padx=40,pady=20,command=lambda:button_click(2))
button_3=Button(base,text="3",padx=42,pady=20,command=lambda:button_click(3))
button_4=Button(base,text="4",padx=40,pady=20,command=lambda:button_click(4))
button_5=Button(base,text="5",padx=40,pady=20,command=lambda:button_click(5))
button_6=Button(base,text="6",padx=42,pady=20,command=lambda:button_click(6))
button_7=Button(base,text="7",padx=40,pady=20,command=lambda:button_click(7))
button_8=Button(base,text="8",padx=40,pady=20,command=lambda:button_click(8))
button_9=Button(base,text="9",padx=42,pady=20,command=lambda:button_click(9))
button_0=Button(base,text="0",padx=40,pady=20,command=lambda:button_click(0))

button_add=Button(base,text="+",padx=39,pady=20,command=button_add)
button_equal=Button(base,text="=",padx=91,pady=20,command=button_equal)
button_clear=Button(base,text="Clear",padx=79,pady=20,command=button_clear)

button_subtract=Button(base,text="-",padx=41,pady=20,command=button_subtract)
button_divide=Button(base,text="/",padx=42,pady=20,command=button_divide)
button_multiply=Button(base,text="*",padx=42,pady=20,command=button_multiply)


button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=0)

button_add.grid(row=5,column=0)
button_clear.grid(row=4,column=1,columnspan=2)
button_equal.grid(row=5,column=1,columnspan=2)

button_subtract.grid(row=6,column=0)
button_divide.grid(row=6,column=1)
button_multiply.grid(row=6,column=2)

base.configure(background="light blue")


base.mainloop()