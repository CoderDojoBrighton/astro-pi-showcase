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

# Add coa = (255, 255, 255) # White
p = (255, 163, 177) # Pink
r = (237, 28, 36) # Red
y = (255, 221, 0) # Yellow
s = (0, 0, 0) # Svart
w = (255, 255, 255) # White
b = (0, 255, 221) # Blue
o = (255, 126, 0) # Orange

for i in range(28):
    rgb = sense.color # get the colour from the sensor
    p = (rgb.red, rgb.green, rgb.blue)

    image = [
      p, p, p, r, p, p, p, p,
      p, p, s, s, s, p, p, p,
      p, s, b, w, b, s, p, p,
      s, s, w, o, w, s, s, p,
      p, s, w, w, w, s, p, p,
      p, s, w, w, w, s, p, p,
      p, s, w, w, w, s, p, p,
      p, p, y, s, y, p, p, p]

    sense.set_pixels(image)
    sleep(1)

# Display the image
p = (255, 163, 177)  # choose your own red, green, blue values between 0 - 255
sense.clear(p)



