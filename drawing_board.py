# -*- coding:utf-8 -*-

import sys
from PyQt5.QtWidgets import (QApplication,QWidget)
from PyQt5.QtGui import (QPainter,QPen)
from PyQt5.QtCore import Qt

class Example(QWidget):
    def __init__(self):
        super(Example,self).__init__()
        self.resize(400,300)
        self.move(100,100)
        self.setWindowTitle("简单的画板1.0")
        self.setMouseTracking(False)
        self.pos_x = 20
        self.pos_y = 20

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        pen = QPen(Qt.black,2,Qt.SolidLine)
        painter.setPen(pen)
        painter.drawLine(20,20,self.pos_x,self.pos_y)
        painter.end()

    def mouseMoveEvent(self, event):
        self.pos_x = event.pos().x()
        self.pos_y = event.pos().y()
        self.update()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    pyqt_learn = Example()
    pyqt_learn.show()
    app.exec_()