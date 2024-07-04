# Import the libraries
from sense_hat import SenseHat
from time import sleep

# Set up the Sense HAT
sense = SenseHat()
sense.set_rotation(270, False)

# Set up the colour sensor
sense.color.gain = 64 # Set the sensitivity of the sensor
sense.color.integration_cycles = 64 # The interval at which the reading will be taken

# Add colour variables and image

lg = (168, 230, 29) # Light green 
b = (156, 90, 60) # Brown
g = (34, 177, 76) # Green
y = (255, 242, 0) # Yellow
o = (255, 194, 14) # Orange
c = (0, 191, 255) # DeepSkyBlue

for i in range(25):
    rgb = sense.color # get the colour from the sensor
    c = (rgb.red, rgb.green, rgb.blue) # use the sensed colour
    
    image = [
      c, c, y, y, y, c, c, c,
      c, y, o, b, o, y, c, c,
      c, c, y, y, y, c, c, c,
      c, c, c, lg, c, c, c, c,
      c, c, c, c, lg, c, c, c,
      c, c, c, g, c, c, c, c,
      c, c, c, c, g, c, c, c,
      b, b, b, g, b, b, b, b]


    sense.set_pixels(image)
    sleep(1)
x = (178, 34, 34)
sense.clear(x)
