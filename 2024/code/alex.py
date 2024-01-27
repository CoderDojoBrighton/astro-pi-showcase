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

s = (0, 191, 255) # DeepSkyBlue
o = (0, 0, 205) # MediumBlue
# Display the image

for i in range(25):

 rgb = sense.color
 s = (rgb.red, rgb.green, rgb.blue)

 image = [
   s, s, s, s, s, s, s, s,
   s, s, s, s, s, s, s, s,
   s, s, s, s, s, s, s, s,
   s, s, s, s, s, s, s, s,
   s, o, o, s, s, o, o, s,
   o, o, s, s, o, o, o, s,
   o, o, o, s, o, o, s, o,
   o, o, o, o, o, o, o, o]

 sense.set_pixels(image)

 sleep(0.2)

 image = [
   s, s, s, s, s, s, s, s,
   s, s, s, s, s, s, s, s,
   s, s, s, s, s, s, s, s,
   s, s, s, s, s, s, s, s,
   s, s, o, o, s, s, o, o,
   s, o, o, s, s, o, o, o,
   s, o, o, o, s, o, o, s,
   o, o, o, o, o, o, o, o]

 sense.set_pixels(image)

 sleep(0.2)

 image = [
   s, s, s, s, s, s, s, s,
   s, s, s, s, s, s, s, s,
   s, s, s, s, s, s, s, s,
   s, s, s, s, s, s, s, s,
   o, s, s, o, o, s, s, o,
   s, s, o, o, s, s, o, o,
   o, s, o, o, o, s, o, o,
   o, o, o, o, o, o, o, o]

 sense.set_pixels(image)

 sleep(0.2)

 image = [
   s, s, s, s, s, s, s, s,
   s, s, s, s, s, s, s, s,
   s, s, s, s, s, s, s, s,
   s, s, s, s, s, s, s, s,
   o, o, s, s, o, o, s, s,
   o, s, s, o, o, s, s, o,
   o, o, s, o, o, o, s, o,
   o, o, o, o, o, o, o, o]
 
 sense.set_pixels(image)

 sleep(0.2)

