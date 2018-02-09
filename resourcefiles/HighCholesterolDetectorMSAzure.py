import http.client, urllib.request, urllib.parse, urllib.error, base64
import cv2
import json

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

body = open("normaleye.jpg", 'rb')


try:
    print("Reading image..")
    image = cv2.imread("normaleye.jpg")
    cv2.imshow("Image",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    conn = http.client.HTTPSConnection("southcentralus.api.cognitive.microsoft.com")
    conn.request("POST", "/customvision/v1.1/Prediction/1f25e3faf08d43d7a5b844a094a0e658/image?%s" % params, body, headers)
    # print("POST", "/customvision/v1.1/Prediction/1f25e3faf08d43d7a5b844a094a0e658/image?%s" % params, body, headers)
    response = conn.getresponse()
    data = response.read()
    # print(data)
    json_data = json.loads(data)
    # print(json_data)
    # print("The type is ",type(json_data))
    # print("The length is ",len(json_data))
    print(json_data)
    for tag in range(len(json_data)):
        print("The chance of ",json_data['Predictions'][tag]['Tag'],"is:")
        print("Probability is: ",round(json_data['Predictions'][tag]['Probability']*100,2),"%")
        # if json_data['Predictions'][tag]['Probability']*100<=10:
        #     print("Proabability is less than 10%")
        # else:
        #     print("Probability is: ",round(json_data['Predictions'][tag]['Probability']*100,2),"%")
    # print(json_data['Predictions'][0]['Tag'])
    # print(json_data['Predictions'][0]['Probability'])
    
    
    conn.close()
except Exception as e:
    print(e)
    # print("An error occured")
    