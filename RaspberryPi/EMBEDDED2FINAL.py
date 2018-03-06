import sys
import PyQt5
import http.client, urllib.request, urllib.parse, urllib.error, base64
import json

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi

from picamera.array import PiRGBArray
from picamera import PiCamera
import time

import pymysql

#OPENCV
import cv2
import numpy as np


#FIRST WINDOW
class App(QMainWindow):

    def __init__(self):
        super().__init__() 
        self.title= "HIGH CHOLESTEROL DETECTOR"
        
        #full screen
        #self.appli = QApplication([])  
        #self.screenie = self.appli.desktop().availableGeometry(-1)
        #self.width, self.height = self.screenie.width(), self.screenie.height()

        self.initUI()

        #Set frame to center
        self.qtRectangle = self.frameGeometry()
        self.centerPoint = QDesktopWidget().screenGeometry(-1).center()
        self.qtRectangle.moveCenter(self.centerPoint)
        self.move(self.qtRectangle.topLeft())


    def initUI(self):
        self.setWindowTitle(self.title)
        
        #GUI size
        self.setGeometry(50,50,500,300) # sets the x & y position, length, and width
        self.setFixedSize(500,300)

        # this block of code sets the background image
        oimg = QImage("window2.jpg") # this is where the image is specified
        simg = oimg.scaled(QSize(500, 300))
        palette = QPalette()
        palette.setBrush(10, QBrush(oimg))
        self.setPalette(palette) # this is used to specify the GUI background image


        # In GUI Python, these buttons, textboxes, labels are called Widgets
        self.okButton = QPushButton('ADMIN', self)
        self.okButton.setToolTip("You've hovered over me!")
        self.okButton.resize(150,50)
        self.okButton.move(185,150)  # button.move(x,y)
        self.okButton.clicked.connect(self.switchWindow)
        self.okButton.setStyleSheet("""
        QPushButton {background-color: rgba(63, 127, 191, 1); 
        color: white; border-style: outset;
        border-width: 0.3px;
        border-radius: 10px;
        border-color: beige;
        min-width: 4em;
        max-width: 10em;
        max-height: 2em;
        min-height: 1em;
        padding: 7px;
        font-size: 14px;
        font-weight: bold;
        font-family: "";}
        QPushButton:hover { background-color: blue; }
        QPushButton:pressed{background-color: rgba(63, 127, 191, 0.4); border-style: inset;}""")

        self.cancelButton = QPushButton('Exit', self)
        self.cancelButton.setToolTip("Click to Exit")
        self.cancelButton.resize(150,50)
        self.cancelButton.move(185, 215)  # button.move(x,y)
        self.cancelButton.clicked.connect(self.closeWindow)
        self.cancelButton.setStyleSheet("""
        QPushButton {background-color: rgba(63, 191, 127, 1); color: white; border-style: outset;
        border-width: 0.3px;
        border-radius: 10px;
        border-color: beige;
        min-width: 4em;
        max-width: 10em;
        max-height: 2em;
        min-height: 1em;
        padding: 7px;
        font-size: 14px;
        font-weight: bold;
        }
        QPushButton:hover { background-color: green; }
        QPushButton:pressed{background-color: rgba(63, 127, 191, 0.4); border-style: inset;}""")

        self.show()

    def switchWindow(self):#PANG TAWAG SA IBANG WINDOW
        self.second = Dialog()
        self.close()

    def closeWindow(self):#PANG TAWAG SA CLOSE
          #MESSAGEBOX  
        reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QMessageBox.Yes | 
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.close()
        else:
            self.show()

#SECOND WINDOW
class Dialog(QDialog):

    def __init__(self):
        super().__init__()

        loadUi('form.ui',self)
        self.title= "HIGH CHOLESTEROL DETECTOR"


        # this block of code sets the background image
        oimg = QImage("window7.jpg") # this is where the image is specified
        palette = QPalette()
        palette.setBrush(10, QBrush(oimg))
        self.setPalette(palette) # this is used to specify the GUI background image

        #Set frame to center
        self.qtRectangle = self.frameGeometry()
        self.centerPoint = QDesktopWidget().screenGeometry(-1).center()
        self.qtRectangle.moveCenter(self.centerPoint)
        self.move(self.qtRectangle.topLeft())

        #textLabels

        #Buttons
        self.ok_Button.clicked.connect(self.thirdwin)
        self.cancel_Button.clicked.connect(self.cancel)

        self.show()

    @pyqtSlot()
    def thirdwin(self):

        #RadioButton GENDER
        if self.female_radio.isChecked():
            self.gender = self.female_radio.text()
        else:
            self.gender = self.male_radio.text()

        #Error handling
        self.enteredage = int(self.age_text.text())
        if self.enteredage >= 20 and self.enteredage <= 60:
            self.age = self.enteredage
            
            #Name
            self.name = self.name_text.text()
            #Address
            self.address = self.address_text.text()

            #Contact error handling
            self.contact = self.contact_text.text()
            if self.contact[0] == '0': 
                if len(self.contact) == 11:

                    #Message
                    QMessageBox.information(self,"Text Data","Name: {} \nGender: {} \nAge: {} \nContact: {} \nAddress: {}".format(self.name, self.gender,
                                                                                            self.age,
                                                                                            self.contact,
                                                                                            self.address),
                                        QMessageBox.Ok,QMessageBox.Ok)
                    #jump to next window
                    self.thirdi = imagecapture()

                    self.close()
                else:
                    #print("Invalid Contact Number")
                    QMessageBox.warning(self,"Warning", "Invalid Contact number, Input valid number",
                        QMessageBox.NoButton, QMessageBox.NoButton)

                #Address
            else:
                QMessageBox.warning(self,"Warning", "Invalid Contact, number must start at 09",
                    QMessageBox.NoButton, QMessageBox.NoButton)
                #print("Invalid Contact Number")

        else:
            QMessageBox.warning(self,"Warning", "Invalid Age",
                QMessageBox.NoButton, QMessageBox.NoButton)
            #print("Invalid Input")

        
    def cancel(self):
        reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QMessageBox.Yes | 
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.third = App()
            self.close()
        else:
            self.show()


class imagecapture(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(50,50,500,300) # sets the x & y position, length, and width
        #self.setFixedSize(800,480)
        self.setWindowTitle("High Cholesterol Analyzer")
        
        # this block of code sets the background image
        oimg = QImage("background.jpg") # this is where the image is specified
        palette = QPalette()
        palette.setBrush(10, QBrush(oimg))
        self.setPalette(palette) # this is used to specify the GUI background image

       
        self.okButton = QPushButton('Capture', self)
        self.okButton.resize(100,50)
        self.okButton.move(50,100)  # button.move(x,y)
        self.okButton.clicked.connect(self.cam)

        self.cButton = QPushButton('Cancel', self)
        self.cButton.resize(100,50)
        self.cButton.move(50, 250)  # button.move(x,y)
        self.cButton.clicked.connect(self.close)
            
        self.show()
 

    def cam(self):
        
##        print("Creating a camera instance")
        camera = PiCamera()
        camera.brightness = 60
        camera.resolution = (640, 480)
        camera.framerate = 32
        rawCapture = PiRGBArray(camera, size=(640, 480))
        # allow the camera to warmup
        time.sleep(0.1)
##        print("Entering loop")
##        # capture frames from the camera
##        for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
##            # grab the raw NumPy array representing the image, then initialize the timestamp
##            # and occupied/unoccupied text
##            image = frame.array
## 
##            # show the frame
##            cv2.imshow("Frame", image)
##            key = cv2.waitKey(1) & 0xFF
## 
##            # clear the stream in preparation for the next frame
##            rawCapture.truncate(0)
## 
##            # if the `q` key was pressed, break from the loop
##            if key == ord("q"):
##                break
        
        # grab an image from the camera
        camera.capture(rawCapture, format="bgr")
        image = rawCapture.array
        #cv2.imshow('Capture Frame', image)
        cv2.imwrite("out.jpg",image)
##        cv2.waitKey(0)
##        cv2.destroyAllWindows()
        print("Loading acceptance class")
        self.acceptancewindow = acceptance("out.jpg")
##        print("Displaying Image")
##        img = cv2.imread("normaleye.jpg")
##        cv2.imshow("normal eye",img) 
##        cv2.waitKey(0)
##        cv2.destroyAllWindows()
        self.close()

    # def switchWindow(self):
    #     self.fourth = QWidget()
    #     self.close()

    # def switchWindow(self):
    #     self.fifth = Dialog()
    #     self.close()

    # def switchwindow(self):
    #     self.acceptancewindow = acceptance()
    #     self.close()
        
class acceptance(QWidget):
#FUNCTION SA BUTTON NA ANALYZE
    def analyzeImage(self, imagepath):
        print("analyzeImage function")
        headers = {
            # Request headers
            'Content-Type': 'application/octet-stream',
            'Prediction-key': '2420e45f2ac54973bbb404bc64a0a5c4',
        }

        params = urllib.parse.urlencode({
            # Request parameters
            'application': 'Embedded2',
            # 'iterationId': '54b5827fe35c425e8e1f41ad596603b9',
        })
        print("Opening imagepath")
        body = open(imagepath, 'rb')
        


        try:
            print("Reading image..")
##            image = cv2.imread(imagepath)
##            cv2.imshow("Image",image)
##            cv2.waitKey(0)
##            cv2.destroyAllWindows()
            print("Performing Request")
            conn = http.client.HTTPSConnection("southcentralus.api.cognitive.microsoft.com")
            conn.request("POST", "/customvision/v1.1/Prediction/1f25e3faf08d43d7a5b844a094a0e658/image?%s" % params, body, headers)
            print("Request Done")
            response = conn.getresponse()
            print("Getting response")
            data = response.read()
            print("Loading data to JSON")

            json_data = json.loads(data.decode('utf-8')) # in linux add .decode('utf-8')

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
        self.analyzeImage(self.inputimage)

    def __init__(self,imagepath):
        super().__init__() 
        self.title= "HIGH CHOLESTEROL DETECTOR"
        self.setFixedWidth(500)
        self.setFixedHeight(300)
        self.x=200 # or left
        self.y=200 # or top
        #self.width= 640
        #self.height= 480
        
        #full screen
        self.appli = QApplication([])  
        self.screenie = self.appli.desktop().availableGeometry(-1)
        self.width, self.height = self.screenie.width(), self.screenie.height()
 
        # self.cam()
        self.inputimage=imagepath

        #Set frame to center
        self.qtRectangle = self.frameGeometry()
        self.centerPoint = QDesktopWidget().screenGeometry(-1).center()
        self.qtRectangle.moveCenter(self.centerPoint)
        self.move(self.qtRectangle.topLeft())



    # def cam(self):
        
    #     cap = cv2.VideoCapture(0)
    #     fourcc = cv2.VideoWriter_fourcc(*'XVID')
    #     while(cap.isOpened()):
    #         ret, frame = cap.read()
    #         if ret==True:
    #             cv2.imwrite('out.jpg', frame)
    #             cv2.imshow('frame',frame)
    #             if cv2.waitKey(1) & 0xFF == ord('q'):
    #                 break   
    #         else:
    #             break

    # # Release everything if job is finished
    #     cap.release()
    #     cv2.destroyAllWindows()

        self.initUI()



    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.x,self.y,self.width,self.height)

       
        self.okButton = QPushButton('Retake', self)
        self.okButton.resize(100,50)
        self.okButton.move(50,150)  # button.move(x,y)
        self.okButton.clicked.connect(self.switchWindow)

        self.cButton = QPushButton('Analyze', self)
        self.cButton.resize(100,50)
        self.cButton.move(50, 50)  # button.move(x,y)
        self.cButton.clicked.connect(self.Analyze)

        
        self.show()

    def switchWindow(self):
        self.fourth = QWidget()
        self.close()

    # def switchWindow(self):
    #     self.fifth = Dialog()
   
    #     self.show()


if __name__=='__main__':
    app = QApplication(sys.argv)
    main = App()
sys.exit(app.exec())
