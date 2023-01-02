from imageFunctions import *
import os
import time


def main():
    # Clear all old files.
    delete_all_files_in_directory("tempImages")
    delete_all_files_in_directory("greenTempImages")

    # iterate through the gifs in the folder 'gif_toConvert'.
    gif_path = ""
    for gif in os.listdir("gifToConvert"):
        gif_path = "gifToConvert/" + gif

        print("Extracting PNGs from .gif.")
        convert_gif_to_pngs(gif_path, "tempImages/" + gif)

        print("Adding green screen to PNGs.")
        for filename in os.listdir("tempImages"):
            f = "tempImages/" + filename
            add_green_to_png(f, "greenTempImages/" + filename)

    print("Converting green screen pngs to new .gif.")
    convert_pngs_to_gif(gif_path)

    print("Converting .gif to MP4")
    convert_gif_to_mp4("png_to_gif.gif", gif_path)


if __name__ == "__main__":
    main()





