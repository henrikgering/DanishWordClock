import time
import board
import neopixel
import math

# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 256 

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB

class LedStrip():

    def __init__(self):
        self.pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=1, auto_write=False, pixel_order=ORDER
)
    pixel_row_start=[
        [234,235],[236,237],[238,239],[240,241],[242,243],[244,245],[246,247],[248,249],[250,251],[252,253],[254,255],
        [229,228],[227,226],[225,224],[223,222],[221,220],[219,218],[217,216],[215,214],[213,212],[211,210],[209,208],
        [182,183],[184,185],[186,187],[188,189],[190,191],[192,193],[194,195],[196,197],[198,199],[200,201],[202,203],
        [177,176],[175,174],[173,172],[171,170],[169,168],[167,166],[165,164],[163,162],[161,160],[159,158],[157,156],
        [130,131],[132,133],[134,135],[136,137],[138,139],[140,141],[142,143],[144,145],[146,147],[148,149],[150,151],
        [125,124],[123,122],[121,120],[119,118],[117,116],[115,114],[113,112],[111,110],[109,108],[107,106],[105,104],
        [78, 79], [80, 81], [82,83],[84,85],[86,87],[88,89],[90,91],[92,93],[94,95],[96,97],[98,99],
        [73, 72], [71, 70], [69,68],[67,66],[65,64],[63,62],[61,60],[59,58],[57,56],[55,54],[53,52],
        [26, 27], [28, 29], [30,31],[32,33],[34,35],[36,37],[38,39],[40,41],[42,43],[44,45],[46,47],
        [21, 20], [19, 18], [17,16],[15,14],[13,12],[11,10],[9,8],[7,6],[5,4],[3,2],[1,0]]

    def turn_all_off(self):
        print("Turning all pixels off");
        self.pixels.fill((0,0,0))
        self.pixels.show()

    indicesThatShouldBeOn=[0]

    i=1
    def ManipulateLeds(self,indicesThatShouldBeOn):
        self.i = (self.i+1)%num_pixels
        self.pixels.fill((0,0,0))
        for letter_number in indicesThatShouldBeOn:
            x = self.pixel_row_start[letter_number]
            for i in x:
                self.pixels[i]=wheel(self.i & 255)

        self.pixels.show()
        self.indicesThatShouldBeOn=indicesThatShouldBeOn
       

def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos * 3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos * 3)
        g = 0
        b = int(pos * 3)
    else:
        pos -= 170
        r = 0
        g = int(pos * 3)
        b = int(255 - pos * 3)
    return (r, g, b) if ORDER in (neopixel.RGB, neopixel.GRB) else (r, g, b, 0)