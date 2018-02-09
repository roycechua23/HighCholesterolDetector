import sys
import cv2
import numpy as np
import http.client, urllib.request, urllib.parse, urllib.error, base64
import json
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class MainScreen(QMainWindow):

    def analyzeImage(self, imagepath):
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
            return Results
            conn.close()
        except Exception as e:
            print(e)
            # print("An error occured")

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

        self.imageLabel = QLabel('',self)
        self.imageLabel.setBackgroundRole(QPalette.Base)
        
        self.image = QImage("normaleye.jpg")
        iconpixm3 = QPixmap.fromImage(self.image)
        iconpics3 = iconpixm3.scaled(QSize(400, 200))
        self.imageLabel.setPixmap(iconpics3)
        self.scaleFactor = 1.0

        self.imageLabel.move(210, 50)
        self.imageLabel.setFixedHeight(250)
        self.imageLabel.setFixedWidth(500)
        
        self.resultLabel = QLabel("Analysis: ",self)
        self.resultLabel.move(120, 200)
        self.resultLabel.setFixedHeight(250)
        self.resultLabel.setFixedWidth(1000)
        self.resultLabel.setStyleSheet("""QLabel{color: White; font-size: 30px;}

                """)
        self.mainLayout = QHBoxLayout()
        self.mainLayout.addWidget(self.imageLabel)
        self.mainLayout.addWidget(self.resultLabel)
        # self.sideLayout = QVBoxLayout()
        
        # self.mainLayout.addWidget()
        QMessageBox.information(self, "Analysis Result",
                                        "\n"+self.analyzeImage("normaleye.jpg"))
        
        self.exitButton = QPushButton("Exit",self)
        self.exitButton.move(350,400)
        self.exitButton.clicked.connect(self.close)
        self.show() # this is used to show the contents of the window
        


app = QApplication(sys.argv)
main = MainScreen()
sys.exit(app.exec())