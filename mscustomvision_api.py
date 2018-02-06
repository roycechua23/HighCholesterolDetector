import http.client, urllib.request, urllib.parse, urllib.error, base64

headers = {
    # Request headers
    'Content-Type': 'application/octet-stream',
    'Prediction-key': '2420e45f2ac54973bbb404bc64a0a5c4',
}

params = urllib.parse.urlencode({
    # Request parameters
    'application': 'Embedded2',
    'iterationId': '146138b6ca4c473ab74631f586e703f6',
    
})

body = open("arcus-senilis.jpg", 'rb')


try:
    conn = http.client.HTTPSConnection("southcentralus.api.cognitive.microsoft.com")
    conn.request("POST", "/customvision/v1.1/Prediction/1f25e3faf08d43d7a5b844a094a0e658/image?%s" % params, body, headers)
    # print("POST", "/customvision/v1.1/Prediction/1f25e3faf08d43d7a5b844a094a0e658/image?%s" % params, body, headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print(e)
    # print("An error occured")
    