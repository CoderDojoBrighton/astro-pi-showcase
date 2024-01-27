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
b = (9, 194, 227) # blue
lb = (217, 151, 98) # light brown
db = (156, 90, 60) # dark brown
lo = (235, 131, 28) # light orange
do = (247, 105, 2) # dark orange
g = (34, 177, 76) # green
p = (203, 15, 255) # purple
r = (176, 42, 35) # red
y = (255, 242, 0) # yellow

for i in range(28):

    rgb = sense.color # get the colour from the sensor
    p = (rgb.red, rgb.green, rgb.blue) # use the sensed colour
    
    image = [
      b, p, p, p, b, b, b, y,
      p, p, r, p, p, b, b, b,
      b, p, p, p, b, b, b, b,
      b, b, g, b, b, b, db, do,
      b, b, g, b, c, b, do, db,
      b, b, g, b, r, r, r, r,
      db, lb, lb, lb, lb, db, db, db,
      lb, db, lb, db, lb, lb, db, db]
    
    # Display the image
    sense.set_pixels(image)
    sleep(1)
sense.clear()
x = (178, 34, 34)  # choose your own red, green, blue values between 0 - 255
sense.clear(x)
