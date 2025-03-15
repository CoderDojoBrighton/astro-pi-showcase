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
br=(156,90,60)
y=(255,242,0)
r=(237,28,36)
w=(255,255,255)
for i in range(28):
    rgb=sense.color
    b=(rgb.red,rgb.green,rgb.blue)
    bl=(0,0,0)
    # Display the image
    image=[
        b,b,b,b,b,b,b,b,
        b,y,y,y,y,y,y,y,
        b,y,y,bl,y,bl,y,y,
        b,y,y,y,y,y,y,y,
        b,y,br,w,r,w,br,y,
        b,y,br,br,br,br,br,y,
        b,b,b,y,b,y,b,b,
        b,b,bl,bl,b,bl,bl,b]
    sense.set_pixels(image)
    sleep(1)
    x=(0,128,64)
sense.clear(x)