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
rl = (237,28 ,36 ) # red light
rd = (153,0 ,48 ) # red dark
y = (255,242 ,0 ) # yellow
b = (156,90 ,60 ) # brown
g = (34,177 ,76 ) # green
bl = (153,217 ,234 ) # blue
lg = (168,230 ,29 ) # light green
# Display the image
for i in range(7):
    rgb = sense.color # get the colour from the sensor
    e = (rgb.red, rgb.green, rgb.blue) # use the sensed colour
    image = [
      e, e, e, rl, e, rl, e, e,
      e, e, rl, rd, rl, rd, rl, e,
      e, e, e, rl, y, rl, e, e,
      e, e, rl, rd, b, rd, rl, e,
      e, e, e, e, b, e, e, e,
      e, e, e, e, b, e, e, e,
      g, g, g, g, g, g, g, g,
      g, g, g, g, g, g, g, g]
    
    sense.set_pixels(image)
    sleep(1)


   

image = [
  bl, bl, bl, g, bl, g, bl, bl,
  bl, bl, g, g, g, bl, bl, bl,
  bl, g, g, g, g, g, g, bl,
  bl, g, g, g, g, g, g, bl,
  bl, bl, bl, g, bl, bl, bl, bl,
  bl, bl, bl, lg, bl, bl, bl, bl,
  bl, bl, bl, lg, bl, bl, bl, bl,
  bl, bl, bl, bl, bl, bl, bl, bl]

sense.set_pixels(image)
sleep(7)
for i in range(7):
    rgb = sense.color # get the colour from the sensor
    e = (rgb.red, rgb.green, rgb.blue) # use the sensed colour
    image = [
      e, e, e, rl, e, rl, e, e,
      e, e, rl, rd, rl, rd, rl, e,
      e, e, e, rl, y, rl, e, e,
      e, e, rl, rd, b, rd, rl, e,
      e, e, e, e, b, e, e, e,
      e, e, e, e, b, e, e, e,
      g, g, g, g, g, g, g, g,
      g, g, g, g, g, g, g, g]
    
    sense.set_pixels(image)
    sleep(1)


   

image = [
  bl, bl, bl, g, bl, g, bl, bl,
  bl, bl, g, g, g, bl, bl, bl,
  bl, g, g, g, g, g, g, bl,
  bl, g, g, g, g, g, g, bl,
  bl, bl, bl, g, bl, bl, bl, bl,
  bl, bl, bl, lg, bl, bl, bl, bl,
  bl, bl, bl, lg, bl, bl, bl, bl,
  bl, bl, bl, bl, bl, bl, bl, bl]

sense.set_pixels(image)
sleep(7)
