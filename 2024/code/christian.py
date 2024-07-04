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
c = (34, 139, 34) # ForestGreen
m = (0, 0, 0) # Black
w = (255, 102, 255) # Pink

# Display the image
for i in range(2):
    rgb = sense.color # get the colour from the sensor
    c = (rgb.red, rgb.green, rgb.blue)
    
    image = [
      c, c, c, c, c, c, c, c,
      c, c, c, c, c, c, c, c,
      c, c, c, c, c, c, c, c,
      c, c, c, c, c, c, c, c,
      c, c, c, c, c, c, c, c,
      c, c, c, c, c, c, c, c,
      c, c, c, c, c, c, c, c,
      c, c, m, w, c, c, c, c]

    sense.set_pixels(image)
    sleep(0.25) 


for i in range(2):
    rgb = sense.color # get the colour from the sensor
    c = (rgb.red, rgb.green, rgb.blue)
    
    image = [
      c, c, c, c, c, c, c, c,
      c, c, c, c, c, c, c, c,
      c, c, c, c, c, c, c, c,
      c, c, c, c, c, c, c, c,
      c, c, c, c, c, c, c, c,
      c, c, c, c, c, c, c, c,
      c, c, m, w, c, c, c, c,
      c, c, w, m, c, c, c, c]

    sense.set_pixels(image)
    sleep(0.25)

for i in range(2):
    rgb = sense.color # get the colour from the sensor
    c = (rgb.red, rgb.green, rgb.blue)
    
    image = [
      c, c, c, c, c, c, c, c,
      c, c, c, c, c, c, c, c,
      c, c, c, c, c, c, c, c,
      c, c, c, c, c, c, c, c,
      c, c, c, c, c, c, c, c,
      c, c, m, w, c, c, c, c,
      c, c, w, m, c, c, c, c,
      c, c, w, w, c, c, c, c]

    sense.set_pixels(image)
    sleep(0.25)

for i in range(2):
    rgb = sense.color # get the colour from the sensor
    c = (rgb.red, rgb.green, rgb.blue)
    
    image = [
      c, c, c, c, c, c, c, c,
      c, c, c, c, c, c, c, c,
      c, c, c, c, c, c, c, c,
      c, c, c, c, c, c, c, c,
      c, c, c, c, c, c, c, c,
      c, c, w, m, w, c, c, c,
      c, c, w, w, m, c, c, c,
      c, c, w, w, c, c, c, c]

    sense.set_pixels(image)
    sleep(0.25)

for i in range(2):
    rgb = sense.color # get the colour from the sensor
    c = (rgb.red, rgb.green, rgb.blue)
    
    image = [
      c, c, c, c, c, c, c, c,
      c, c, c, c, c, c, c, c,
      c, c, c, c, c, c, c, c,
      c, c, c, c, c, c, c, c,
      c, c, c, c, c, c, c, c,
      c, c, w, w, m, w, c, c,
      c, c, w, w, w, m, c, c,
      c, c, w, w, c, c, c, c]

    sense.set_pixels(image)
    sleep(0.25)

for i in range(2):
    rgb = sense.color # get the colour from the sensor
    c = (rgb.red, rgb.green, rgb.blue)
    
    image = [
      c, c, c, c, c, c, c, c,
      c, c, c, c, c, c, c, c,
      c, c, c, c, c, c, c, c,
      c, c, c, c, c, c, c, c,
      c, c, c, c, c, c, c, c,
      c, c, w, w, w, m, w, c,
      c, c, w, w, w, w, m, c,
      c, c, w, w, c, c, c, c]

    sense.set_pixels(image)
    sleep(0.25)

for i in range(2):
    rgb = sense.color # get the colour from the sensor
    c = (rgb.red, rgb.green, rgb.blue)
    
    image = [
      c, c, c, c, c, c, c, c,
      c, c, c, c, c, c, c, c,
      c, c, c, c, c, c, c, c,
      c, c, c, c, c, c, c, c,
      c, c, c, c, c, m, w, c,
      c, c, w, w, w, w, m, c,
      c, c, w, w, w, w, w, c,
      c, c, w, w, c, c, c, c]

    sense.set_pixels(image)
    sleep(0.25)

for i in range(2):
    rgb = sense.color # get the colour from the sensor
    c = (rgb.red, rgb.green, rgb.blue)
    
    image = [
      c, c, c, c, c, c, c, c,
      c, c, c, c, c, c, c, c,
      c, c, c, c, c, c, c, c,
      c, c, c, c, c, m, w, c,
      c, c, c, c, c, w, m, c,
      c, c, w, w, w, w, w, c,
      c, c, w, w, w, w, w, c,
      c, c, w, w, c, c, c, c]

    sense.set_pixels(image)
    sleep(0.25)

for i in range(2):
    rgb = sense.color # get the colour from the sensor
    c = (rgb.red, rgb.green, rgb.blue)
    
    image = [
      c, c, c, c, c, c, c, c,
      c, c, c, c, c, c, c, c,
      c, c, c, c, c, m, w, c,
      c, c, c, c, c, w, m, c,
      c, c, c, c, c, w, w, c,
      c, c, w, w, w, w, w, c,
      c, c, w, w, w, w, w, c,
      c, c, w, w, c, c, c, c]

    sense.set_pixels(image)
    sleep(0.25)

for i in range(2):
    rgb = sense.color # get the colour from the sensor
    c = (rgb.red, rgb.green, rgb.blue)
    
    image = [
      c, c, c, c, c, c, c, c,
      c, c, c, c, c, m, w, c,
      c, c, c, c, c, w, m, c,
      c, c, c, c, c, w, w, c,
      c, c, c, c, c, w, w, c,
      c, c, w, w, w, w, w, c,
      c, c, w, w, w, w, w, c,
      c, c, w, w, c, c, c, c]

    sense.set_pixels(image)
    sleep(0.25)

for i in range(2):
    rgb = sense.color # get the colour from the sensor
    c = (rgb.red, rgb.green, rgb.blue)
    
    image = [
      c, c, c, c, c, c, c, c,
      c, c, c, c, m, w, w, c,
      c, c, c, c, w, m, w, c,
      c, c, c, c, c, w, w, c,
      c, c, c, c, c, w, w, c,
      c, c, w, w, w, w, w, c,
      c, c, w, w, w, w, w, c,
      c, c, w, w, c, c, c, c]

    sense.set_pixels(image)
    sleep(0.25)

for i in range(2):
    rgb = sense.color # get the colour from the sensor
    c = (rgb.red, rgb.green, rgb.blue)
    
    image = [
      c, c, c, c, c, c, c, c,
      c, c, c, m, w, w, w, c,
      c, c, c, w, m, w, w, c,
      c, c, c, c, c, w, w, c,
      c, c, c, c, c, w, w, c,
      c, c, w, w, w, w, w, c,
      c, c, w, w, w, w, w, c,
      c, c, w, w, c, c, c, c]

    sense.set_pixels(image)
    sleep(0.25)

for i in range(2):
    rgb = sense.color # get the colour from the sensor
    c = (rgb.red, rgb.green, rgb.blue)
    
    image = [
      c, c, c, m, w, c, c, c,
      c, c, c, w, m, w, w, c,
      c, c, c, w, w, w, w, c,
      c, c, c, c, c, w, w, c,
      c, c, c, c, c, w, w, c,
      c, c, w, w, w, w, w, c,
      c, c, w, w, w, w, w, c,
      c, c, w, w, c, c, c, c]

    sense.set_pixels(image)
    sleep(0.25)

for i in range(2):
    rgb = sense.color # get the colour from the sensor
    c = (rgb.red, rgb.green, rgb.blue)
    
    image = [
      c, c, c, w, m, c, c, c,
      c, c, c, w, w, w, w, c,
      c, c, c, w, w, w, w, c,
      c, c, c, c, c, w, w, c,
      c, c, c, c, c, w, w, c,
      c, c, w, w, w, w, w, c,
      c, c, w, w, w, w, w, c,
      c, c, c, c, c, c, c, c]

    sense.set_pixels(image)
    sleep(0.25)

for i in range(2):
    rgb = sense.color # get the colour from the sensor
    c = (rgb.red, rgb.green, rgb.blue)
    
    image = [
      c, c, c, w, w, c, c, c,
      c, c, c, w, w, w, w, c,
      c, c, c, w, w, w, w, c,
      c, c, c, c, c, w, w, c,
      c, c, c, c, c, w, w, c,
      c, c, c, w, w, w, w, c,
      c, c, c, w, w, w, w, c,
      c, c, c, c, c, c, c, c]

    sense.set_pixels(image)
    sleep(0.25)

for i in range(2):
    rgb = sense.color # get the colour from the sensor
    c = (rgb.red, rgb.green, rgb.blue)
    
    image = [
      c, c, c, w, w, c, c, c,
      c, c, c, w, w, w, w, c,
      c, c, c, w, w, w, w, c,
      c, c, c, c, c, w, w, c,
      c, c, c, c, c, w, w, c,
      c, c, c, c, w, w, w, c,
      c, c, c, c, w, w, w, c,
      c, c, c, c, c, c, c, c]

    sense.set_pixels(image)
    sleep(0.25)

for i in range(2):
    rgb = sense.color # get the colour from the sensor
    c = (rgb.red, rgb.green, rgb.blue)
    
    image = [
      c, c, c, w, w, c, c, c,
      c, c, c, w, w, w, w, c,
      c, c, c, w, w, w, w, c,
      c, c, c, c, c, w, w, c,
      c, c, c, c, c, w, w, c,
      c, c, c, c, c, w, w, c,
      c, c, c, c, c, w, w, c,
      c, c, c, c, c, c, c, c]

    sense.set_pixels(image)
    sleep(0.25)

for i in range(2):
    rgb = sense.color # get the colour from the sensor
    c = (rgb.red, rgb.green, rgb.blue)
    
    image = [
      c, c, c, w, w, c, c, c,
      c, c, c, w, w, w, w, c,
      c, c, c, w, w, w, w, c,
      c, c, c, c, c, w, w, c,
      c, c, c, c, c, w, w, c,
      c, c, c, c, c, w, w, c,
      c, c, c, c, c, c, c, c,
      c, c, c, c, c, c, c, c]

    sense.set_pixels(image)
    sleep(0.25)

for i in range(2):
    rgb = sense.color # get the colour from the sensor
    c = (rgb.red, rgb.green, rgb.blue)
    
    image = [
      c, c, c, w, w, c, c, c,
      c, c, c, w, w, w, w, c,
      c, c, c, w, w, w, w, c,
      c, c, c, c, c, w, w, c,
      c, c, c, c, c, w, w, c,
      c, c, c, c, c, c, c, c,
      c, c, c, c, c, c, c, c,
      c, c, c, c, c, c, c, c]

    sense.set_pixels(image)
    sleep(0.25)

for i in range(2):
    rgb = sense.color # get the colour from the sensor
    c = (rgb.red, rgb.green, rgb.blue)
    
    image = [
      c, c, c, w, w, c, c, c,
      c, c, c, w, w, w, w, c,
      c, c, c, w, w, w, w, c,
      c, c, c, c, c, w, w, c,
      c, c, c, c, c, c, c, c,
      c, c, c, c, c, c, c, c,
      c, c, c, c, c, c, c, c,
      c, c, c, c, c, c, c, c]

    sense.set_pixels(image)
    sleep(0.25)

for i in range(2):
    rgb = sense.color # get the colour from the sensor
    c = (rgb.red, rgb.green, rgb.blue)
    
    image = [
      c, c, c, w, w, c, c, c,
      c, c, c, w, w, w, w, c,
      c, c, c, w, w, w, w, c,
      c, c, c, c, c, c, c, c,
      c, c, c, c, c, c, c, c,
      c, c, c, c, c, c, c, c,
      c, c, c, c, c, c, c, c,
      c, c, c, c, c, c, c, c]

    sense.set_pixels(image)
    sleep(0.25)

for i in range(2):
    rgb = sense.color # get the colour from the sensor
    c = (rgb.red, rgb.green, rgb.blue)
    
    image = [
      c, c, c, w, w, c, c, c,
      c, c, c, w, w, w, c, c,
      c, c, c, w, w, w, c, c,
      c, c, c, c, c, c, c, c,
      c, c, c, c, c, c, c, c,
      c, c, c, c, c, c, c, c,
      c, c, c, c, c, c, c, c,
      c, c, c, c, c, c, c, c]

    sense.set_pixels(image)
    sleep(0.25)

for i in range(2):
    rgb = sense.color # get the colour from the sensor
    c = (rgb.red, rgb.green, rgb.blue)
    
    image = [
      c, c, c, w, w, c, c, c,
      c, c, c, w, w, c, c, c,
      c, c, c, w, w, c, c, c,
      c, c, c, c, c, c, c, c,
      c, c, c, c, c, c, c, c,
      c, c, c, c, c, c, c, c,
      c, c, c, c, c, c, c, c,
      c, c, c, c, c, c, c, c]

    sense.set_pixels(image)
    sleep(0.25)

for i in range(2):
    rgb = sense.color # get the colour from the sensor
    c = (rgb.red, rgb.green, rgb.blue)
    
    image = [
      c, c, c, w, w, c, c, c,
      c, c, c, w, w, c, c, c,
      c, c, c, c, c, c, c, c,
      c, c, c, c, c, c, c, c,
      c, c, c, c, c, c, c, c,
      c, c, c, c, c, c, c, c,
      c, c, c, c, c, c, c, c,
      c, c, c, c, c, c, c, c]

    sense.set_pixels(image)
    sleep(0.25)

for i in range(2):
    rgb = sense.color # get the colour from the sensor
    c = (rgb.red, rgb.green, rgb.blue)
    
    image = [
      c, c, c, w, w, c, c, c,
      c, c, c, c, c, c, c, c,
      c, c, c, c, c, c, c, c,
      c, c, c, c, c, c, c, c,
      c, c, c, c, c, c, c, c,
      c, c, c, c, c, c, c, c,
      c, c, c, c, c, c, c, c,
      c, c, c, c, c, c, c, c]

    sense.set_pixels(image)
    sleep(0.25)

for i in range(2):
    rgb = sense.color # get the colour from the sensor
    c = (rgb.red, rgb.green, rgb.blue)
    
    image = [
      c, c, c, c, c, c, c, c,
      c, c, c, c, c, c, c, c,
      c, c, c, c, c, c, c, c,
      c, c, c, c, c, c, c, c,
      c, c, c, c, c, c, c, c,
      c, c, c, c, c, c, c, c,
      c, c, c, c, c, c, c, c,
      c, c, c, c, c, c, c, c]

    sense.set_pixels(image)
    sleep(1)

    
x = (34, 139, 34)  # choose your own red, green, blue values between 0 - 255
sense.clear(x)   
