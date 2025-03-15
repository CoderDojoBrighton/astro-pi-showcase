# Import the libraries
from sense_hat import SenseHat
from time import sleep

# Set up the Sense HAT
sense = SenseHat()
sense.set_rotation(270, False)

# Set up the colour sensor
sense.color.gain = 60 # Set the sensitivity of the sensor
sense.color.integration_cycles = 64 # The interval at which the reading will be taken

b = (156, 90, 60)
d = (255, 163, 177)
f = (0, 0, 0) # Black
e = (255, 255, 255)
g = (0, 183, 239)
h = (255, 194, 14)

for i in range(28):
    rgb = sense.color # get the colour from the sensor
    c = (rgb.red, rgb.green, rgb.blue) # use the sensed colour
    
    image = [
      c, b, c, c, c, b, c, c,
      b, d, b, c, b, d, b, c,
      b, d, b, b, b, d, b, c,
      b, e, f, b, f, e, b, c,
      c, e, f, d, f ,e ,b ,c,
      g, g, g, g, g, g, g, c,
      b, b, b, b, h, h, b, c,
      b, b, b, b, b, b, b, c]
    
    # Display the image
    sense.set_pixels(image)
    sleep(1)
sense.clear()
x = (156, 90, 60)  # choose your own red, green, blue values between 0 - 255
sense.clear(x)