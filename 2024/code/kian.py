# Import the libraries
from sense_hat import SenseHat
from time import sleep

# Set up the Sense HAT
sense = SenseHat()
sense.set_rotation(270, False)

# Set up the colour sensor
sense.color.gain = 60 # Set the sensitivity of the sensor
sense.color.integration_cycles = 64 # The interval at which the reading will be taken

# Add colour variables and image
b = (77,109,243)#blue
o = (255,126,0)#orange
c = (0,0,0)#black
y = (255,194,14)#yellow
for i in range(28):
    rgb = sense.color
    c = (rgb.red, rgb.green, rgb.blue)
    # Display the image
    image = [
    b, b, b, c, b, c, b, b,
    b, b, o, o, o, o, b, b,
    b, o, y, o, y, o, b, b,
    b, o, o, o, o, o, b, b,
    b, b, b, y, y, o, b, b,
    b, b, o, y, o, y, b, o,
    b, b, b, y, y, o, o, b,
    b, b, b, o, b, o, b, b,
    ]
    sense.set_pixels(image)
    sleep(1)