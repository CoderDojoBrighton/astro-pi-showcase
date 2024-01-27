# Import the libraries
from sense_hat import SenseHat
from time import sleep

# Set up the Sense HAT
sense = SenseHat()
sense.set_rotation(270, False)

# Set up the colour sensor
sense.color.gain = 64 # Set the sensitivity of the sensor
sense.color.integration_cycles = 64 # The interval at which the reading will be taken
sense.low_light = True

# Add colour variables and image
d = (100, 149, 237) # CornflowerBlue
m = (34, 139, 34) # ForestGreen
q = (255, 255, 0) # Yellow
s = (139, 69, 19) # SaddleBrown

for i in range(26):
    rgb = sense.color # get the colour from the sensor
    d = (rgb.red, rgb.green, rgb.blue) # use the sensed colour

    image =[
    d,d,d,d,d,d,q,q,
    d,d,d,d,d,d,q,q,    
    d,d,m,m,m,d,d,d,
    d,m,m,m,m,m,d,d,
    d,d,d,s,d,d,d,m,
    d,d,d,s,d,m,m,s,
    m,m,m,m,m,s,s,s,
    s,s,s,s,s,s,s,s]

    # Display the image
    sense.set_pixels(image)
    sleep (1)

x=(178, 34, 34) # Firebrick
sense.clear(x)
