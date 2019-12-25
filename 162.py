# -*- coding: utf-8 -*-
import sys
import random
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QMainWindow


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)

a = {'Audi': 'TT', 'BMW': 'Nazca', 'Henessy': 'Venom GT', 'Ford': 'GT40','Porsche': '356A',
     'Volvo': '850R', 'Subaru': 'WRX STI', 'Alfa Romeo': 'TZ2', 'Noble': 'M600'}
b = ['TT', 'Nazca', '356A', '850R', 'Venom GT', 'GT40', 'WRX STI', 'TZ2', 'M600']

class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('aud.ui', self)
        self.count = 0
        self.buttons = [self.pushButton_2, self.pushButton_3, self.pushButton_4, self.pushButton]
        self.titles = set()
        self.pushButton_5.clicked.connect(self.clear_and_start)
        self.pushButton_2.clicked.connect(self.check)
        self.pushButton_3.clicked.connect(self.check)
        self.pushButton_4.clicked.connect(self.check)
        self.pushButton.clicked.connect(self.check)
        
    
    def clear_and_start(self):
        self.count = 0
        self.run()


    def run(self):
        self.titles.clear()
        self.flag = 0
        self.label.setText(random.choice(list(a.keys())))
        self.label_2.setText(str(self.count))
        for i in self.buttons:
            number = random.randint(0, 100)
            if ((number in range(80, 100)) or (i == self.pushButton)) and (not(self.flag)):
                i.setText(a[self.label.text()])
                self.titles.add(a[self.label.text()])
                self.flag = 1
            else:
                n = random.choice(b)
                while n in self.titles or n == a[self.label.text()]:
                    n = random.choice(b)
                i.setText(n)
                self.titles.add(n)  
                
    def check(self):
        if self.sender().text() == a[self.label.text()]:
            self.count += 1
            self.label_2.setText(str(self.count))
        self.run()
            
            
            

sys.excepthook = except_hook
app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())