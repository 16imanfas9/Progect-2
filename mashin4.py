from tkinter import*
import math
class calculate:
    
    def __init__(self,call):
        self.call=call
        self.call.title('my second calculat')
        self.display=Entry(call,width=20,borderwidth=6,textvariable=StringVar(),font=('arial',14),bg='lightblue')
        self.display.grid(row=0,column=0,columnspan=4,padx=10,pady=10)
        self.total=StringVar(call)
        self.creat_button()
    
    def click_button(self,value):
        currnt=self.display.get()
        self.display.delete(0,END)
        self.display.insert(0,currnt+str(value))
        if value=='sqrt':
            result=math.sqrt(float(currnt))
            self.display.delete(0,END)
            self.display.insert(0,result)
        elif value=='sin':
            result=math.sin(math.radians(float(currnt)))
            self.display.delete(0,END)
            self.display.insert(0,result)
        elif value=='cos': 
            result=math.cos(math.radians(float(currnt)))
            self.display.delete(0,END)
            self.display.insert(0,result)
        elif value=='tan':
            result=math.tan(math.radians(float(currnt)))
            self.display.delete(0,END)
            self.display.insert(0,result)
        elif value=='^2':
            result=(float(currnt))**2
            self.display.delete(0,END)
            self.display.insert(0,result)
        elif value=='log':
            result=math.log(float(currnt))
            self.display.delete(0,END)
            self.display.insert(0,result)
    def add_clear(self):
        operator=self.display.get()    
        self.display.delete((0,END)[:-1])   
        
    def calclator(self):
        try:
            result=eval(self.display.get())
            self.display.delete(0,END)
            self.display.insert(0,str(result))
        except Exception as e:
            self.display.delete(0,END)
            self.display.insert(0,'Error') 
    
    def creat_button(self):
        buttons=[
            ('7',1,0),('8',1,1),('9',1,2),('0',1,3),
            ('6',2,0),('5',2,1),('4',2,2),('+',2,3),
            ('3',3,0),('2',3,1),('1',3,2),('-',3,3),
            ('*',4,0),('/',4,1),('.',4,2),
            ('log',5,2),('cos',5,3),('sin',6,0),('sq',6,1),
            ('tan',6,2),('^2',6,3)
        ]
        
        for (text,row,col) in buttons:
            buttn=Button(self.call,text=text,bg='white',width=8,height=3,command=lambda t=text:self.click_button(t))
            buttn.grid(row=row,column=col)

        self.clear_button=Button(self.call,text='c',width=8,height=3,bg='white',command=lambda:self.display.delete(0,END))
        self.clear_button.grid(row=5,column=0)
        self.equal_button=Button(self.call,text='=',width=8,height=3,bg='cyan',command=self.calclator)
        self.equal_button.grid(row=5,column=1)
        self.acbutton=Button(self.call,text='Ac',width=8,height=3,bg='lightblue',command=self.add_clear)
        self.acbutton.grid(row=4,column=3)
if __name__=='__main__':
    call=Tk()
    iamg=calculate(call)
    call.mainloop()
    
    
