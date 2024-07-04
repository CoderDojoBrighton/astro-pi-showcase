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
br=(229,170,122)
pi=(255,163,177)
black=(0,0,0)
blu=(153,217,91)
gra=(180,180,180)
gre=(211,249,188)
ye=(255,249,189)
sun=(245,228,156)
for i in range(28):
#    rgb=sense.color
#    blu=(rgb.red,rgb.green,rgb.blue)
    # Display the image
    image=[blu,blu,br,blu,blu,blu,sun,sun,
           ye,br,br,blu,blu,blu,sun,sun,
           ye,black,br,br,br,blu,blu,blu,
           ye,pi,pi,br,br,br,blu,blu,
           blu,blu,br,br,br,br,br,blu,
           blu,br,br,br,br,br,br,blu,
           blu,gra,blu,gra,gra,br,br,blu,
           gre,gre,gre,gre,gre,gre,gre,gre
        
    ]
    sense.set_pixels(image)
    sleep(1)
