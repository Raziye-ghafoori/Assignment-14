from math import *
import sympy
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtUiTools import QUiLoader


class Calculator (QMainWindow):
    def __init__(self):
        super().__init__()

        loader=QUiLoader()
        self.app=loader.load("Calculator.ui")
        self.app.show()

        self.result=0
        self.lastOp=""

        self.app.Zero.clicked.connect(self.number0)
        self.app.One.clicked.connect(self.number1)
        self.app.Two.clicked.connect(self.number2)
        self.app.Three.clicked.connect(self.number3)
        self.app.Four.clicked.connect(self.number4)
        self.app.Five.clicked.connect(self.number5)
        self.app.Six.clicked.connect(self.number6)
        self.app.Seven.clicked.connect(self.number7)
        self.app.Eight.clicked.connect(self.number8)
        self.app.Nine.clicked.connect(self.number9)

        self.app.Add.clicked.connect(self.add)
        self.app.Submission.clicked.connect(self.sub)
        self.app.Multiplication.clicked.connect(self.multi)
        self.app.Division.clicked.connect(self.divi)
        self.app.Sin.clicked.connect(self.sinx)
        self.app.Cos.clicked.connect(self.cosx)
        self.app.Tan.clicked.connect(self.tanx)
        self.app.Cot.clicked.connect(self.cotx)
        self.app.Log.clicked.connect(self.logx)
        self.app.Sqrt.clicked.connect(self.sqrtx)
        self.app.Dot.clicked.connect(self.dot)
        self.app.Mark.clicked.connect(self.mark)
        self.app.Equal.clicked.connect(self.equal)
        self.app.Delet.clicked.connect(self.clear)



    def add(self):
        try:
            self.resalt=float(self.app.TB.text())
            self.app.TB.setText("")
            self.lastOp="+"
        except:
            self.app.TB.setText("Error")
            self.result = 0
        
    def sub(self):
        try:
            self.resalt=float(self.app.TB.text())
            self.app.TB.setText("")
            self.lastOp="-"
        except:
            self.app.TB.setText("Error")
            self.result = 0
       

    def multi(self):
        try:
            self.resalt=float(self.app.TB.text())
            self.app.TB.setText("")
            self.lastOp="*"
        except:
            self.app.TB.setText("Error")
            self.result = 0
        

    def divi(self):
        try:
            self.resalt=float(self.app.TB.text())
            self.app.TB.setText("")
            self.lastOp="/"
        except:
            self.app.TB.setText("Error")
            self.result = 0
        

    def sinx(self):
        if sin(radians(float(self.app.TB.text()))) >1:
            self.app.TB.setText("+∞")
        elif sin(radians(float(self.app.TB.text()))) <-1:
            self.app.TB.setText("-∞")
        else:
             self.app.TB.setText(str(round(sin(radians(float(self.app.TB.text()))))))

    def cosx(self):
             self.app.TB.setText(str(round(cos(radians(float(self.app.TB.text()))))))

    def tanx(self):
        if tan(radians(float(self.app.TB.text()))) >1:
            self.app.TB.setText("+∞")
        elif tan(radians(float(self.app.TB.text()))) <-1:
            self.app.TB.setText("-∞")
        else:
             self.app.TB.setText(str(tan(radians(float(self.app.TB.text())))))

    def cotx(self):
        if sympy.cot(radians(float(self.app.TB.text()))) >1:
            self.app.TB.setText("+∞")
        elif sympy.cot(radians(float(self.app.TB.text())))<-1:
            self.app.TB.setText("-∞")
        else:
            self.app.TB.setText(str(round(sympy.cot(radians(float(self.app.TB.text()))))))

    def logx(self):
        self.app.TB.setText(str(log10(float(self.app.TB.text()))))

    def sqrtx(self):
        self.app.TB.setText(str(sqrt(float(self.app.TB.text()))))

    def dot(self):
        if '.' not in self.app.TB.text():
            self.app.TB.setText(self.app.TB.text() + '.')

    def clear(self):
       self.app.TB.setText("")
       self.resalt=0
       self.lastOp=""
    
    def mark(self):
        self.n2=float(self.app.TB.text())
        self.n2 *=-1
        self.app.TB.setText(str(self.n2))

    def equal(self):
        self.n2 = float(self.app.TB.text())
        
        if self.lastOp == "+":
            self.resalt +=self.n2
            self.app.TB.setText(str(self.resalt))
            self.lastOp= ""
            self.result=0
        elif self.lastOp == "-":
            self.resalt -=self.n2
            self.app.TB.setText(str(self.resalt))
            self.lastOp= ""
            self.result=0
        elif self.lastOp == "*":
            self.resalt *= self.n2
            self.app.TB.setText(str(self.resalt))
            self.lastOp= ""
            self.result=0
        elif self.lastOp == "/":
            try:
                self.resalt /= self.n2
                self.app.TB.setText(str(self.resalt))
                self.lastOp= ""
                self.result=0
            except:
                self.app.TB.setText("Error")
                self.lastOp= ""
                self.result=0
        else:
            self.result = self.n2

        

    def number0(self):
        self.app.TB.setText(self.app.TB.text() + "0")
    def number1(self):
        self.app.TB.setText(self.app.TB.text() + "1")
    def number2(self):
        self.app.TB.setText(self.app.TB.text() + "2")
    def number3(self):
        self.app.TB.setText(self.app.TB.text() + "3")
    def number4(self):
        self.app.TB.setText(self.app.TB.text() + "4")
    def number5(self):
        self.app.TB.setText(self.app.TB.text() + "5")
    def number6(self):
        self.app.TB.setText(self.app.TB.text() + "6")
    def number7(self):
        self.app.TB.setText(self.app.TB.text() + "7")
    def number8(self):
        self.app.TB.setText(self.app.TB.text() + "8")
    def number9(self):
        self.app.TB.setText(self.app.TB.text() + "9")



if __name__ == "__main__":
    my_app=QApplication()
    main_window=Calculator()
    my_app.exec()