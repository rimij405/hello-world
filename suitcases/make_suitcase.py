from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import fraction as f
import os

"""
Set of functions that are used to generate and manage suitcase images for use in baggage claim
"""
__author__ = "jks743"

def makecase(filename, color, frac):
    suitcase = Image.open('suitcase.png')
    if not os.path.exists('cases'):
        os.mkdir('cases')
    suitcase = suitcase.convert("RGBA")
    suit_data = suitcase.getdata()

    new_data = []

# here we're replacing white wit hour given color
    for item in suit_data:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            new_data.append(color)
        else:
            new_data.append(item)
    
    suitcase.putdata(new_data)

    # now we can put our text onto the image
    numerator = str(frac.numerator)
    denominator = str(frac.denominator)
    suitcase_draw = ImageDraw.Draw(suitcase)

    # chosen text size of 60
    font = ImageFont.truetype("TruenoSBd.otf", size=60)

    # calculation to findthe appropriate place to put our text
    suitcase_draw.text((233 - (20 * (len(numerator) - 1)), 200),numerator,fill='black', font=font)

    suitcase_draw.text((233 - (20 * (len(denominator) - 1)), 275),denominator,fill='black', font=font)
    # make our image file
    dir_string = "cases/" + filename
    suitcase.save(dir_string, "PNG")


"""
Clears the current set of images generated
"""
def clear():
    os.rmtree("/cases")


fract_test = f.Fraction(30, 40)
makecase("blah.png", (255,0,0,255), fract_test)
