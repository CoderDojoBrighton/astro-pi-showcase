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
y=(255,242,0)
v=(181,165,213)
lg=(168,230,29)
for i in range(28):
    rgb = sense.color # get the colour from the sensor
    b = (rgb.red, rgb.green, rgb.blue) # use the sensed colour
    # Display the image
    image=[
    b,b,b,b,b,b,b,b,
    b,b,v,v,v,b,b,b,
    b,v,y,y,v,v,b,b,
    b,v,v,v,v,b,b,b,
    b,b,lg,b,b,b,b,b,
    b,b,lg,lg,b,b,b,b,
    b,lg,lg,b,b,b,b,b,
    b,b,lg,b,b,b,b,b    
    ]
    sense.set_pixels(image)
    sleep(1)
sense.clear()