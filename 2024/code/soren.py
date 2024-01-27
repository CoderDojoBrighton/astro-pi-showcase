# Import the libraries
from sense_hat import SenseHat
from time import sleep

# Set up the Sense HAT
sense = SenseHat()
sense.set_rotation(270, False)

# Set up the colour sensor
sense.color.gain = 64 # Set the sensitivity of the sensor
sense.color.integration_cycles = 64 # The interval at which the reading will be taken

print ("Made by Soren,")
c = (0, 0, 0) # Black
g = (0, 191, 255) # DeepSkyBlue
m = (34, 139, 34) # ForestGreen
n = (154, 205, 50) # YellowGreen
q = (255, 255, 0) # Yellow
t = (255, 140, 0) # DarkOrange
v = (255, 0, 0) # Red

y = (255, 20, 147) # DeepPink

for i in range(2):
    # Add colour variables and image
   
    rgb = sense.color # get the colour from the sensor
    c = (rgb.red, rgb.green, rgb.blue)
    # Display the image
    image = [
        q, q, c, c, c, c, c, c,
        q, q, c, c, c, c, c, c,
        c, c, c, c, c, c, c, c,
        c, c, c, c, c, c, c, c,
        c, c, c, c, c, c, c, c,
        c, c, c, c, c, c, c, c,
        c, c, c, c, c, n, c, c,
        m, m, m, m, m, m, m, m,]
    # Display the image
    sense.set_pixels(image)
    sleep(1)

for i in range(2):
    # Add colour variables and image   
    rgb = sense.color # get the colour from the sensor
    c = (rgb.red, rgb.green, rgb.blue)
    # Display the image
    image = [
        q, q, c, c, c, c, c, c,
        q, q, c, c, c, c, c, c,
        c, c, c, c, c, c, c, c,
        c, c, c, c, c, c, c, c,
        c, c, c, c, c, c, c, c,
        c, c, c, c, c, n, c, c,
        c, c, c, c, c, n, c, c,
        m, m, m, m, m, m, m, m,]

    # Display the image
    sense.set_pixels(image)
    sleep(1)
   
x = (0, 251, 255)  # choose your own red, green, blue values between 0 - 255
sense.clear(x)

for i in range(2):
    # Add colour variables and image
   
    rgb = sense.color # get the colour from the sensor
    c = (rgb.red, rgb.green, rgb.blue)
    # Display the image
    image = [
        q, q, c, c, c, c, c, c,
        q, q, c, c, c, c, c, c,
        c, c, c, c, c, c, c, c,
        c, c, c, c, c, c, c, c,
        c, c, c, c, c, n, c, c,
        c, c, c, c, n, n, c, c,
        c, c, c, c, c, n, c, c,
        m, m, m, m, m, m, m, m,]
    # Display the image
    sense.set_pixels(image)
    sleep(1)

for i in range(2):
    # Add colour variables and image
   
    rgb = sense.color # get the colour from the sensor
    c = (rgb.red, rgb.green, rgb.blue)
    # Display the image
    image = [
        t, q, c, c, c, c, c, c,
        q, q, c, c, c, q, c, c,
        c, c, c, c, q, t, q, c,
        c, c, c, c, c, q, c, c,
        c, c, c, c, c, n, n, c,
        c, c, c, c, n, n, c, c,
        c, c, c, c, c, n, c, c,
        m, m, m, m, m, m, m, m,]
    # Display the image
    sense.set_pixels(image)
    sleep(1)

for i in range(2):
    # Add colour variables and image
   
    rgb = sense.color # get the colour from the sensor
    c = (rgb.red, rgb.green, rgb.blue)
    # Display the image
    image = [
        t, q, c, c, q, q, q, c,
        q, q, c, q, t, t, t, q,
        c, c, c, q, t, v, t, q,
        c, c, c, q, t, t, t, q,
        c, c, c, c, q, q, q, c,
        c, c, c, c, c, n, c, c,
        c, c, c, c, c, n, c, c,
        m, m, m, m, m, m, m, m,]

    # Display the image
    sense.set_pixels(image)
    sleep(1)

for i in range(2):
    # Add colour variables and image
    
    rgb = sense.color # get the colour from the sensor
    c = (rgb.red, rgb.green, rgb.blue)
    # Display the image
    image = [
        g, g, q, q, q, q, g, g,
        g, q, q, q, q, q, q, g,
        q, q, t, t, t, t, q, q,
        q, q, t, v, v, t, q, q,
        q, q, t, v, v, t, q, q,
        q, q, t, t, t, t, q, q,
        g, q, q, q, q, q, q, g,
        m, m, q, q, q, q, m, m,]
    # Display the image
    sense.set_pixels(image)
    sleep(1)

for i in range(2):
    # Add colour variables and image
   
    rgb = sense.color # get the colour from the sensor
    c = (rgb.red, rgb.green, rgb.blue)
    # Display the image
    image = [
        c, y, y, c, c, y, y, c,
        y, y, y, y, y, y, y, y,
        y, y, y, y, y, y, y, y,
        y, y, y, y, y, y, y, y,
        c, y, y, y, y, y, y, c,
        c, c, y, y, y, y, c, c,
        c, c, c, y, y, c, c, c,
        c, c, c, c, c, c, c, c,]
    # Display the image
    sense.set_pixels(image)
    sleep(1)

for i in range(2):
    # Add colour variables and image
   
    rgb = sense.color # get the colour from the sensor
    c = (rgb.red, rgb.green, rgb.blue)
    # Display the image
    image = [
        q, q, c, c, c, c, c, c,
        q, q, c, c, c, c, c, c,
        c, c, c, c, c, c, c, c,
        c, c, c, c, c, c, c, c,
        c, c, c, c, c, c, c, c,
        c, c, c, c, c, c, c, c,
        c, c, c, c, c, n, c, c,
        m, m, m, m, m, m, m, m,]
    # Display the image
    sense.set_pixels(image)
    sleep(1)

for i in range(2):
    # Add colour variables and image
   
    rgb = sense.color # get the colour from the sensor
    c = (rgb.red, rgb.green, rgb.blue)
    # Display the image
    image = [
        q, q, c, c, c, c, c, c,
        q, q, c, c, c, c, c, c,
        c, c, c, c, c, c, c, c,
        c, c, c, c, c, c, c, c,
        c, c, c, c, c, c, c, c,
        c, c, c, c, c, n, c, c,
        c, c, c, c, c, n, c, c,
        m, m, m, m, m, m, m, m,]

    # Display the image
    sense.set_pixels(image)
    sleep(1)
   
x = (0, 251, 255)  # choose your own red, green, blue values between 0 - 255
sense.clear(x)

for i in range(2):
    # Add colour variables and image
   
    rgb = sense.color # get the colour from the sensor
    c = (rgb.red, rgb.green, rgb.blue)
    # Display the image
    image = [
        q, q, c, c, c, c, c, c,
        q, q, c, c, c, c, c, c,
        c, c, c, c, c, c, c, c,
        c, c, c, c, c, c, c, c,
        c, c, c, c, c, n, c, c,
        c, c, c, c, n, n, c, c,
        c, c, c, c, c, n, c, c,
        m, m, m, m, m, m, m, m,]
    # Display the image
    sense.set_pixels(image)
    sleep(1)

for i in range(2):
    # Add colour variables and image
   
    rgb = sense.color # get the colour from the sensor
    c = (rgb.red, rgb.green, rgb.blue)
    # Display the image
    image = [
        t, q, c, c, c, c, c, c,
        q, q, c, c, c, q, c, c,
        c, c, c, c, q, t, q, c,
        c, c, c, c, c, q, c, c,
        c, c, c, c, c, n, n, c,
        c, c, c, c, n, n, c, c,
        c, c, c, c, c, n, c, c,
        m, m, m, m, m, m, m, m,]
    # Display the image
    sense.set_pixels(image)
    sleep(1)

for i in range(2):
    # Add colour variables and image
   
    rgb = sense.color # get the colour from the sensor
    c = (rgb.red, rgb.green, rgb.blue)
    # Display the image
    image = [
        t, q, c, c, q, q, q, c,
        q, q, c, q, t, t, t, q,
        c, c, c, q, t, v, t, q,
        c, c, c, q, t, t, t, q,
        c, c, c, c, q, q, q, c,
        c, c, c, c, c, n, c, c,
        c, c, c, c, c, n, c, c,
        m, m, m, m, m, m, m, m,]

    # Display the image
    sense.set_pixels(image)
    sleep(1)

for i in range(2):
    # Add colour variables and image
   
    rgb = sense.color # get the colour from the sensor
    c = (rgb.red, rgb.green, rgb.blue)
    # Display the image
    image = [
        g, g, q, q, q, q, g, g,
        g, q, q, q, q, q, q, g,
        q, q, t, t, t, t, q, q,
        q, q, t, v, v, t, q, q,
        q, q, t, v, v, t, q, q,
        q, q, t, t, t, t, q, q,
        g, q, q, q, q, q, q, g,
        m, m, q, q, q, q, m, m,]
    # Display the image
    sense.set_pixels(image)
    sleep(1)

for i in range(1):
    # Add colour variables and image
   
    rgb = sense.color # get the colour from the sensor
    c = (rgb.red, rgb.green, rgb.blue)
    # Display the image
    image = [
        c, y, y, c, c, y, y, c,
        y, y, y, y, y, y, y, y,
        y, y, y, y, y, y, y, y,
        y, y, y, y, y, y, y, y,
        c, y, y, y, y, y, y, c,
        c, c, y, y, y, y, c, c,
        c, c, c, y, y, c, c, c,
        c, c, c, c, c, c, c, c,]
    # Display the image
    sense.set_pixels(image)
    sleep(1)

print ("Hello Astronauts! 😀")
