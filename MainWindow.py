import sys
import PyQt5
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize  
from PyQt5 import QtCore, QtWidgets
from PyQt5 import QtGui




class App(QMainWindow):

    def __init__(self):
        super().__init__() 
        self.title= "HIGH CHOLESTEROL DETECTOR"
        self.x=200 # or left
        self.y=200 # or top
        #self.width= 640
        #self.height= 480
        
        #full screen
        self.appli = QApplication([])  
        self.screenie = self.appli.desktop().availableGeometry(-1)
        self.width, self.height = self.screenie.width(), self.screenie.height()
 
        self.initUI()

        #Set frame to center
        self.qtRectangle = self.frameGeometry()
        self.centerPoint = QDesktopWidget().screenGeometry(-1).center()
        self.qtRectangle.moveCenter(self.centerPoint)
        self.move(self.qtRectangle.topLeft())

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.x,self.y,self.width,self.height)
        #self.show


        # In GUI Python, these buttons, textboxes, labels are called Widgets
        self.okButton = QPushButton('ADMIN', self)
        self.okButton.setToolTip("You've hovered over me!")
        self.okButton.resize(250,100)
        self.okButton.move(550,250)  # button.move(x,y)
        self.okButton.clicked.connect(self.switchWindow)

        self.cancelButton = QPushButton('Exit', self)
        self.cancelButton.setToolTip("Click to Exit")
        self.cancelButton.resize(250,100)
        self.cancelButton.move(550, 370)  # button.move(x,y)
        self.cancelButton.clicked.connect(self.closeWindow)

        self.show()

    def switchWindow(self):
        self.second = Dialog()
        self.close()

    def closeWindow(self):
        
        reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QMessageBox.Yes | 
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.close()
        else:
            self.show()


class Dialog(QDialog):
    NumGridRows = 10
    NumButtons = 14
 
    def __init__(self):
        super().__init__()
        self.createFormGroupBox()
 
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)
 
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.formGroupBox)
        mainLayout.addWidget(buttonBox)
        self.setMinimumHeight(400)
        self.setMinimumWidth(500)
        self.setMaximumHeight(400)
        self.setMaximumWidth(650)
        self.setLayout(mainLayout)
        self.setWindowTitle("HIGH CHOLESTEROL DETECTOR")


    def createFormGroupBox(self):
      

        self.formGroupBox = QGroupBox("FORM")

        self.radio1 = QRadioButton("Male")
        self.radio2 = QRadioButton("Female")
        self.radio1.setChecked(True)

        layout = QFormLayout()
        layout.addRow(QLabel("Name:"), QLineEdit())
        layout.addRow(QLabel("Gender:"))
        layout.addWidget(self.radio1)
        layout.addWidget(self.radio2)
        layout.addRow(QLabel("Age:"), QSpinBox())
        layout.addRow(QLabel("Contact Number:"), QLineEdit())
        layout.addRow(QLabel("Address:"), QLineEdit())
        self.formGroupBox.setLayout(layout)

        self.show()




app = QApplication(sys.argv)
main = App()
sys.exit(app.exec())