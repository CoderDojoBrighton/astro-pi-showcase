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
for i in range(28):
    rgb=sense.color
    yellow=(255,242,0)
    blue=(rgb.red,rgb.green,rgb.blue)
    green=(34,177,76)
    white=(255,255,255)
    black=(70,70,70)
    grey=(180,180,180)
    # Display the image
    image=[
        white,white,white,white,blue,blue,blue,white,
        blue,white,white,blue,blue,blue,white,white,
        blue,blue,blue,blue,blue,blue,blue,blue,
        blue,blue,blue,blue,blue,blue,black,yellow,
        blue,black,black,black,black,black,black,black,
        black,blue,black,black,black,black,blue,blue,
        blue,blue,black,blue,blue,black,blue,blue,
        green,green,green,green,green,green,green,green
    ]
    sense.set_pixels(image)
    sleep(1)