# Second unused test file, used during troubleshooting flask apps
from picamera2 import *
import time
picam2 = Picamera2()
camera_config = picam2.create_preview_configuration()
picam2.configure(camera_config)
picam2.start()
time.sleep(2)
picam2.capture_file("test.png")
