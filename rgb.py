#!/usr/bin/env python

from flask import Flask
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

app = Flask(__name__)

# Explorer HAT uses GPIO 27 = red, 4 = blue, 5 = green
# Pibrella uses GPIO 27 = red, 17 = yellow, 4 = green


# Map of LED names and associated GPIO pins
leds = {
    'red':    27,
    'blue':   4,
    'green':  5
}

for color in leds.keys():
    GPIO.setup(leds[color], GPIO.OUT)

@app.route("/led/<color>/<state>")
def set_led(color, state):
    if color in leds.keys():
      if state == 'on':
          GPIO.output(leds[color], 1)
          return 'LED On: {}'.format(color)
      else:
          GPIO.output(leds[color], 0)
          return 'LED Off: {}'.format(color)

    return 'Invalid LED: {}'.format(color)

app.add_url_rule("/", "index", lambda: 'Hello World!')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
