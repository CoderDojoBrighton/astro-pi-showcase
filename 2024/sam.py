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
c = (0, 0, 0) # Black
t = (255, 140, 0) # DarkOrange
v = (255, 0, 0) # Red
r = (184, 134, 11) # DarkGoldenrod
b = (105, 105, 105) # DimGray
k = (46, 139, 87) # SeaGreen
l = (0, 255, 127) # SpringGreen
m = (34, 139, 34) # ForestGreen
s = (139, 69, 19) # SaddleBrown
a = (255, 255, 255) # White

for i in range(25):
    rgb = sense.color # get the colour from the sensor
    a = (rgb.red, rgb.green, rgb.blue) # use the sensed colour
    
    if i < 8:   
        image = [
          a, a, a, a, a, a, a, a,
          a, a, a, t, a, r, a, a,
          a, t, t, t, a, v, r, a,
          t, t, c, t, a, t, v, a,
          a, a, t, t, t, v, r, a,
          a, a, r, t, t, r, t, a,
          a, a, a, t, t, v, a, a,
          a, a, t, t, a, a, a, a]
    elif i <18:    
        image = [
          k, v, k, m, k, m, v, m,
          a, k, m, k, m, k, k, s,
          a, a, v, a, k, a, s, v,
          a, a, a, a, a, a, s, s,
          a, a, a, a, a, a, s, s,
          a, a, a, a, a, a, s, s,
          a, a, a, a, a, l, l, l,
          l, l, l, l, l, l, l, l]
    else:
        image = [
          a, a, a, c, m, c, a, a,
          a, c, c, m, c, c, c, a,
          c, v, v, c, c, v, v, c,
          c, v, v, v, v, v, v, c,
          c, v, v, v, v, v, v, c,
          c, v, v, v, v, v, v, c,
          a, c, v, v, v, v, c, a,
          a, a, c, c, c, c, a, a]
          
    sense.set_pixels(image)
    sleep(1)
