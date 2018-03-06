import picamera

camera = picamera.PiCamera()
camera.start_preview()
camera.capture("snapchat.jpg")
