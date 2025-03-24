from flask import Flask, render_template
import RPi.GPIO as GPIO

app = Flask(__name__)

@app.route("/redled_on", methods =["POST"])
def led_on_r():
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	GPIO.setup(18, GPIO.OUT)
	print("Red LED on")
	GPIO.output(18, GPIO.HIGH)
	return "ok"

@app.route("/redled_off", methods=["POST"])
def led_off_r():
	GPIO.output(18, GPIO.LOW)
	print("Red LED off")
	return "ok"

@app.route("/yellowled_on", methods =["POST"])
def led_on_y():
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	GPIO.setup(22, GPIO.OUT)
	print("Yellow LED on")
	GPIO.output(22, GPIO.HIGH)
	return "ok"
@app.route("/yellowled_off", methods=["POST"])
def led_off_y():
	GPIO.output(22, GPIO.LOW)
	print("Yellow LED off")
	return "ok"

@app.route("/", methods=["GET"])
def home():
	return render_template("button.html", title="Button", name="Henry Cussatt")
