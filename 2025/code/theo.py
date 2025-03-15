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
g=(133, 255, 0)
db=(83, 67, 20)
b=(98, 76, 15)
bk=(0, 0, 0)
# Display the image

for i in range(27):
    rgb = sense.color # get the colour from the sensor
    c = (rgb.red, rgb.green, rgb.blue) # use the sensed colour
    
    image = [
      g, g, g, g, g, g, g, g,
      db, b, b, bk, b, db, b, db,
      db, bk, db, db, db, db, b, db,
      b, b, db, b, b, db, b, bk,
      db, db, db, bk, b, bk, db, db,
      bk, b, b, db, b, b, b, db,
      db, db, db, db, bk, db, db, bk,
      bk, bk, b, db, b, db, b, db]
    
    # Display the image
    sense.set_pixels(image)
    sleep(1)
sense.clear()
x = (0, 255, 255)  # choose your own red, green, blue values between 0 - 255
sense.clear(x)