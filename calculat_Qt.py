from PyQt5.QtWidgets import *
from PyQt5 import QtCore,QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import math
import sys

class window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("my calculat with PyQt by (iman fathali)")
        self.setGeometry(100,100,350,370)
        
        self.uiComponents()
        self.show()
    
    def uiComponents(self):
        self.label=QLabel(self)
        self.label.setGeometry(5,5,340,50)
        self.label2=QLabel("programed by (iman fathali)",self)
        self.label2.setAlignment(Qt.AlignCenter)
        self.label2.setFont(QFont("serif",13))
        self.label2.setGeometry(15,60,320,35)
        self.label2.setStyleSheet("QLabel" "{""background:lightblue;""}")
        
        self.label.setWordWrap(True)
        self.label.setStyleSheet("QLabel" "{" "border:1px solid black;""background:lightgreen;""}")
        self.label.setAlignment(Qt.AlignRight)
        self.label.setFont(QFont("arial",15))
        push1=QPushButton("1",self)
        push1.setGeometry(5,100,80,40)
        push2=QPushButton("2",self)
        push2.setGeometry(90,100,80,40)
        push3=QPushButton("3",self)
        push3.setGeometry(175,100,80,40)
        push4=QPushButton("4",self)
        push4.setGeometry(260,100,80,40)
        push5=QPushButton("5",self)
        push5.setGeometry(5,143,80,40)
        push6=QPushButton("6",self)
        push6.setGeometry(90,143,80,40)
        push7=QPushButton("7",self)
        push7.setGeometry(175,143,80,40)
        push8=QPushButton("8",self)
        push8.setGeometry(260,143,80,40)
        push9=QPushButton("9",self)
        push9.setGeometry(5,186,80,40)
        pushzero=QPushButton("0",self)
        pushzero.setGeometry(90,186,80,40)
        pushsub=QPushButton("-",self)
        pushsub.setGeometry(175,186,80,40)
        pushmult=QPushButton("*",self)
        pushmult.setGeometry(260,186,80,40)
        pushdiv=QPushButton("/",self)
        pushdiv.setGeometry(5,229,80,40)
        pushcler=QPushButton("c",self)
        pushcler.setGeometry(90,229,80,40)
        pushadd=QPushButton("+",self)
        pushadd.setGeometry(175,229,80,40)
        pushAC=QPushButton("AC",self)
        pushAC.setGeometry(260,229,80,40)
        pushsqrt=QPushButton("SQ",self)
        pushsqrt.setGeometry(5,272,80,40)
        pushlog=QPushButton("log",self)
        pushlog.setGeometry(90,272,80,40)
        pushsin=QPushButton("sin",self)
        pushsin.setGeometry(175,272,80,40)
        pushequl=QPushButton("=",self)
        pushequl.setGeometry(260,272,80,40)
        pushcosios=QPushButton("cos",self)
        pushcosios.setGeometry(5,313,80,40)
        pushtan=QPushButton("tan",self)
        pushtan.setGeometry(90,313,80,40)
        pushpoint=QPushButton(".",self)
        pushpoint.setGeometry(175,313,80,40)
        pushtavan=QPushButton("^*",self)
        pushtavan.setGeometry(260,313,80,40)
        push1.setStyleSheet("QPushButton" "{""border:1px solid blue""background:blue""}")

        pushsub.clicked.connect(self.action_sub)
        pushadd.clicked.connect(self.action_add)
        pushmult.clicked.connect(self.action_mult)
        pushdiv.clicked.connect(self.action_div)
        pushsqrt.clicked.connect(self.action_sqrt)
        pushsin.clicked.connect(self.action_sin)
        pushcosios.clicked.connect(self.action_cos)
        pushtan.clicked.connect(self.action_tan)
        pushpoint.clicked.connect(self.action_point)
        pushtavan.clicked.connect(self.action_tavan)
        pushlog.clicked.connect(self.action_log)
        pushequl.clicked.connect(self.action_equal)
        pushzero.clicked.connect(self.action_zero)
        push1.clicked.connect(self.action1)
        push2.clicked.connect(self.action2)
        push3.clicked.connect(self.action3)
        push4.clicked.connect(self.action4)
        push5.clicked.connect(self.action5)
        push6.clicked.connect(self.action6)
        push7.clicked.connect(self.action7)
        push8.clicked.connect(self.action8)
        push9.clicked.connect(self.action9)
        pushcler.clicked.connect(self.action_clear)
        pushAC.clicked.connect(self.action_ac)
        

    def action_equal(self):
        equation=self.label.text()
        try:
            ans=eval(equation)
            self.label.setText(str(ans)) 
        except:
            self.label.setText("wrong input")
    def action_sub(self):
        text=self.label.text()
        self.label.setText(text + "-")
    
    def action_add(self):
        text=self.label.text()
        self.label.setText(text + "+")
    
    def action_mult(self):
        text=self.label.text()
        self.label.setText(text + "*")
    
    def action_div(self):
        text=self.label.text()
        self.label.setText(text + "/")
    
    def action_clear(self):
        self.label.setText("")
    
    def action1(self):
        text=self.label.text()
        self.label.setText(text + "1")
    
    def action2(self):
        text=self.label.text()
        self.label.setText(text + "2")

    def action3(self):
        text=self.label.text()
        self.label.setText(text + "3")
    
    def action4(self):
        text=self.label.text()
        self.label.setText(text + "4")
    
    def action5(self):
        text=self.label.text()
        self.label.setText(text + "5")
    
    def action6(self):
        text=self.label.text()
        self.label.setText(text + "6")
    
    def action7(self):
        text=self.label.text()
        self.label.setText(text + "7")
    
    def action8(self):
        text=self.label.text()
        self.label.setText(text + "8")
    
    def action9(self):
        text=self.label.text()
        self.label.setText(text + "9")
    
    def action_zero(self):
        text=self.label.text()
        self.label.setText(text + "0")

    def action_ac(self):
        text=self.label.text()
        print(text[:len(text)-1])
        self.label.setText(text[:len(text)-1])

    def action_sqrt(self):
        text=self.label.text()
        result=math.sqrt(float(text))
        self.label.setText(str(result))

    def action_sin(self):
        text=self.label.text()
        result=math.sin(math.radians(float(text)))
        self.label.setText(str(result))

    def action_cos(self):
        text=self.label.text()
        result=math.cos(math.radians(float(text)))
        self.label.setText(str(result))
    def action_log(self):
        text=self.label.text()
        result=math.log(float(text))
        self.label.setText(str(result))

    def action_tan(self):
        text=self.label.text()
        result=math.tan(float(text))
        self.label.setText(str(result))

    def action_point(self):
        text=self.label.text()
        self.label.setText(text + ".")
    
    def action_tavan(self):
        text=self.label.text()
        self.label.setText(text + "**")
    
    def action(self):
        text=self.label2.text()
        self.label2.setText(text+"imanfathali")

App=QApplication(sys.argv)
window=window()
sys.exit(App.exec())