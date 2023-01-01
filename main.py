from imageFunctions import *
import os
import time

convert_gif_to_pngs("test.gif", "tempImages/")

for filename in os.listdir("tempImages"):
    f = "tempImages/" + filename
    print(f)
    add_green_to_png(f, "greenTempImages/" + filename)

convert_frames_to_video()



