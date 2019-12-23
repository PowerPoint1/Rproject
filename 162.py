# -*- coding: utf-8 -*-
import sys
import random
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QMainWindow



def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)
    
a = {'Audi': 'Q7', 'BMW': 'M5 E92', 'Henessy': 'Venom GT', 'Ford': 'GT40', 'Porsche': 'Macan',
     'Volvo': 'XC60', 'Subaru': 'WRX STI', 'Alfa Romeo': 'TZ2', 'Noble': 'M600'}
b = ['Q7', 'M5 E92', 'Venom GT', 'GT40', 'Macan', 'XC60', 'WRX STI', 'TZ2', 'M600']

class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.count = 0
        uic.loadUi('aud.ui', self)
        self.buttons = [self.pushButton_2, self.pushButton_3, self.pushButton_4, self.pushButton]
        self.titles = set()
        self.pushButton_5.clicked.connect(self.run)
        
    def run(self):
        self.flag = 0
        self.label.setText(random.choice(list(a.keys())))
        for i in self.buttons:
            number = random.randint(0, 100)
            if (number in range(80, 100)) or (i == self.pushButton) and (not(self.flag)):
                i.setText(a[self.label.text()])
                self.flag = 1
            else:
                n = random.choice(b)
                while n in self.titles or n == a[self.label.text()]:
                    n = random.choice(b)    
                i.setText(n)
                self.titles.add(n)            
        
        
        
        
sys.excepthook = except_hook
app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())