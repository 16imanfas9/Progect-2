import tkinter as tk
from tkinter import*
import math
root=tk.Tk()
root.title('calclator by imanfas')
root.geometry('310x530')
root.resizable(0,0)
entrystrvar=StringVar(root)
lbl=tk.Label(root,text='my first calculate(1404)',font=('arial',15))
lbl.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
display=tk.Entry(root,width=19,borderwidth=8,textvariable=entrystrvar,font=('arial',20,'bold'))
display.grid(row=1,column=0,columnspan=4)
btn7=tk.Button(root,text='7',font=('arial',20,'bold'),width=4,height=2,command=lambda:add_button(7))
btn7.grid(row=2,column=0)
btn8=tk.Button(root,text='8',font=('arial',20,'bold'),width=4,height=2,command=lambda:add_button(8))
btn8.grid(row=2,column=1)
btn9=tk.Button(root,text='9',font=('arial',20,'bold'),width=4,height=2,command=lambda:add_button(9))
btn9.grid(row=2,column=2)
btn6=tk.Button(root,text='6',font=('arial',20,'bold'),width=4,height=2,command=lambda:add_button(6))
btn6.grid(row=3,column=0)
btn5=tk.Button(root,text='5',font=('arial',20,'bold'),width=4,height=2,command=lambda:add_button(5))
btn5.grid(row=3,column=1)
btn4=tk.Button(root,text='4',font=('arial',20,'bold'),width=4,height=2,command=lambda:add_button(4))
btn4.grid(row=3,column=2)
btn3=tk.Button(root,text='3',font=('arial',20,'bold'),width=4,height=2,command=lambda:add_button(3))
btn3.grid(row=4,column=0)
btn2=tk.Button(root,text='2',font=('arial',20,'bold'),width=4,height=2,command=lambda:add_button(2))
btn2.grid(row=4,column=1)
btn1=tk.Button(root,text='1',font=('arial',20,'bold'),width=4,height=2,command=lambda:add_button(1))
btn1.grid(row=4,column=2)
btn0=tk.Button(root,text='0',font=('arial',20,'bold'),width=4,height=2,command=lambda:add_button(0))
btn0.grid(row=2,column=3)
btnadd=tk.Button(root,text='+',font=('arial',20,'bold'),bg='lightblue',width=4,height=2,command=lambda:add_button('+'))
btnadd.grid(row=3,column=3)
btnsub=tk.Button(root,text='-',font=('arial',20,'bold'),bg='lightblue',width=4,height=2,command=lambda:add_button('-'))
btnsub.grid(row=4,column=3)
btnmult=tk.Button(root,text='*',font=('arial',20,'bold'),bg='lightblue',width=4,height=2,command=lambda:add_button('*'))
btnmult.grid(row=5,column=0)
btndiv=tk.Button(root,text='/',font=('arial',20,'bold'),bg='lightblue',width=4,height=2,command=lambda:add_button('/'))
btndiv.grid(row=5,column=1)
btneq=tk.Button(root,text='=',font=('arial',20,'bold'),bg='lightblue',width=4,height=2,command=lambda:calculat())
btneq.grid(row=5,column=2)
btnclear=tk.Button(root,text='c',font=('arial',20,'bold'),bg='lightblue',width=4,height=2,command=lambda:clear())
btnclear.grid(row=5,column=3)
btnac=tk.Button(root,text='AC',font=('arial',20),bg='cyan',width=4,height=2,command=lambda:entrystrvar.set(entrystrvar.get()[:-1]))
btnac.grid(row=6,column=0)
btnclear=tk.Button(root,text='sq',font=('arial',20,'bold'),bg='lightgreen',width=4,height=2,command=lambda:add_operation('sq'))
btnclear.grid(row=6,column=1)
btnclear=tk.Button(root,text='sin',font=('arial',20,'bold'),bg='lightgreen',width=4,height=2,command=lambda:add_operation('sin'))
btnclear.grid(row=6,column=2)
btnclear=tk.Button(root,text='cos',font=('arial',20,'bold'),bg='lightgreen',width=4,height=2,command=lambda:add_operation('cos'))
btnclear.grid(row=6,column=3)


def add_button(number):
    currnt=display.get()
    currnt+=str(number)
    display.delete(0,tk.END)
    display.insert(0,currnt)

def add_operation(num):
    currnt=display.get()
    if num=='sq':
        result=math.sqrt(float(currnt))
        display.delete(0,tk.END)
        display.insert(0,result)
    elif num=='sin':
        result=math.sin(math.radians(float(currnt)))
        display.delete(0,tk.END)
        display.insert(0,result)
    elif num=='cos':
        result=math.cos(math.radians(float(currnt)))
        display.delete(0,tk.END)
        display.insert(0,result)

def calculat():
    answer=display.get()
    display.delete(0,tk.END)
    display.insert(0,eval(answer))
def clear():
    display.delete(0,tk.END)





root.mainloop()