
import os
import os.path

from PIL import Image

im = Image.open("./IMG_1881.jpeg")
print(im.format, im.size, im.mode)
