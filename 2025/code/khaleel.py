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
    g=(28,148,62)
    r=(237,28,36)
    b=(156,90,60)
    rgb = sense.color # get the colour from the sensor
    lb= (rgb.red, rgb.green, rgb.blue) # use the sensed colour
    c =(34,177,76)
    o=(255,194,14)
    y=(255,242,0)
    dg=(24,122,52)
    tg=(34,177,76)
    # Display the image
    image=[
        lb,lb,dg,dg,dg,tg,o,y,
        lb,dg,dg,dg,tg,tg,tg,o,
        lb,dg,dg,dg,tg,tg,tg,lb,
        lb,lb,r,dg,dg,tg,lb,lb,
        lb,lb,lb,b,b,r,lb,lb,
        r,r,r,b,b,b,r,dg,
        dg,b,r,b,dg,b,b,dg,
        dg,dg,dg,dg,dg,dg,dg,dg]

    sense.set_pixels(image)
    sleep(1)