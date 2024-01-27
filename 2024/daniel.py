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
m = (216, 27, 96) # madgenta
p = (240, 98, 146) # pink
l = (255, 196, 229) # light pink
g = (34, 177, 76) # green
d = (173, 20, 87) # DeepPink
b = (0, 0, 0) #black
z = (168, 230, 29) #light green
for i in range(28):
    rgb = sense.color # get the colour from the sensor
    b = (rgb.red, rgb.green, rgb.blue)
    image = [
      b, b, b, l, l, b, b, b,
      b, b, p, d, d, p, b, b,
      b, l, m, p, p, d, l, b,
      b, b, d, l, l, d, b, b,
      b, z, m, d, m, m, z, b,
      b, g, z, m, z, g, b, b,
      b, b, g, g, z, g, b, b,
      b, b, b, z, b, b, b, b]
    sense.set_pixels(image)
    sleep(1)
