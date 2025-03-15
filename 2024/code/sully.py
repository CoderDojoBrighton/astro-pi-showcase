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
c = (0, 0, 0) # Black
m = (34, 139, 34) # ForestGreen
q = (255, 255, 0) # Yellow
t = (255, 140, 0) # DarkOrange
y = (255, 20, 147) # DeepPink

for i in range(28):
    rgb = sense.color # get the colour from the sensor
    c = (rgb.red, rgb.green, rgb.blue) # use the sensed colour9

    image = [
      c, c, y, y, y, y, c, c,
      c, y, y, t, t, y, y, c,
      y, y, t, q, q, t, y, y,
      c, y, y, t, t, y, y, c,
      c, c, y, y, y, y, c, c,
      m, c, c, m, m, c, c, m,
      c, m, m, m, m, m, m, c,
      c, c, c, m, m, c, c, c]

# Display the image
    sense.set_pixels(image)
    sleep(1)
    
x = (0, 255, 255)
sense.clear(x)
