# Unused in final program, takes picture and saves it to base file for testing
from flask import Flask, render_template
from picamera2 import Picamera2, Preview
import time
app = Flask(__name__)

@app.route("/photo", methods =["POST"])
def getPicture():
    picam2 = Picamera2()
    camera_config = picam2.create_preview_configuration()
    picam2.configure(camera_config)
    picam2.start()
    time.sleep(2)
    picam2.capture_file("test.jpg")




