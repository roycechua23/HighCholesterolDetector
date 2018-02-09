import sys
import PyQt5
import http.client, urllib.request, urllib.parse, urllib.error, base64
import json

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

#OPENCV
import cv2
import numpy as np


#FIRST WINDOW
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

#SECOND WINDOW
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

    def accept(self):
        self.third = imagecapture()
        #self.third = acceptance()
        #self.dialog = Dialog()
        self.close()

 

#THIRD WINDOW
class imagecapture(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(50,50,800,480) # sets the x & y position, length, and width
        self.setFixedSize(800,480)
        self.setWindowTitle("High Cholesterol Analyzer")
        
        # this block of code sets the background image
        oimg = QImage("background.jpg") # this is where the image is specified
        palette = QPalette()
        palette.setBrush(10, QBrush(oimg))
        self.setPalette(palette) # this is used to specify the GUI background image

        

        self.show()
        
    def switchwindow(self):
        self.acceptancewindow = acceptance()
        self.close()
        
class acceptance(QWidget):

    def analyzeImage(self, imagepath):
        print("analyzeImage function")
        headers = {
            # Request headers
            'Content-Type': 'application/json',
            'Prediction-key': '2420e45f2ac54973bbb404bc64a0a5c4',
        }

        params = urllib.parse.urlencode({
            # Request parameters
            'application': 'Embedded2',
            # 'iterationId': '146138b6ca4c473ab74631f586e703f6',
        })
        print("Opening imagepath")
        body = open(imagepath, 'rb')


        try:
            print("Reading image..")
            image = cv2.imread("normaleye.jpg")
            cv2.imshow("Image",image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

            conn = http.client.HTTPSConnection("southcentralus.api.cognitive.microsoft.com")
            conn.request("POST", "/customvision/v1.1/Prediction/1f25e3faf08d43d7a5b844a094a0e658/image?%s" % params, body, headers)

            response = conn.getresponse()
            data = response.read()

            json_data = json.loads(data)

            print(json_data)
            Results = ""
            for tag in range(len(json_data)):
                print("The chance of ",json_data['Predictions'][tag]['Tag'],"is:")
                print("Probability is: ",round(json_data['Predictions'][tag]['Probability']*100,2),"%")
                Results+="The chance of {} is: {} % \n\n".format(json_data['Predictions'][tag]['Tag'],round(json_data['Predictions'][tag]['Probability']*100,2))
            QMessageBox.information(self, "Analysis Result",
                                        "\n"+Results)
            conn.close()
        except Exception as e:
            print(e)
            # print("An error occured")

    def Analyze(self):
        print("Load this function")
        self.analyzeImage("eye.jpg")

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
 
        self.cam()

        #Set frame to center
        self.qtRectangle = self.frameGeometry()
        self.centerPoint = QDesktopWidget().screenGeometry(-1).center()
        self.qtRectangle.moveCenter(self.centerPoint)
        self.move(self.qtRectangle.topLeft())



    def cam(self):
        
        cap = cv2.VideoCapture(0)
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        while(cap.isOpened()):
            ret, frame = cap.read()
            if ret==True:
                cv2.imwrite('out.jpg', frame)
                cv2.imshow('frame',frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break   
            else:
                break

    # Release everything if job is finished
        cap.release()
        cv2.destroyAllWindows()

        self.initUI()



    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.x,self.y,self.width,self.height)

       
        self.okButton = QPushButton('Retake', self)
        self.okButton.resize(750,50)
        self.okButton.move(350,750)  # button.move(x,y)
        self.okButton.clicked.connect(self.switchWindow)

        self.cancelButton = QPushButton('Analyze', self)
        self.cancelButton.resize(750,50)
        self.cancelButton.move(350, 800)  # button.move(x,y)
        self.cancelButton.clicked.connect(self.Analyze)

        
        self.show()

    def switchWindow(self):
        self.fourth = QWidget()
        self.close()

    def switchWindow(self):
        self.fifth = Dialog()
   
        self.show()


if __name__=='__main__':
    app = QApplication(sys.argv)
    main = App()
sys.exit(app.exec())
