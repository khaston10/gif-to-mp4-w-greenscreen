from PIL import Image
import numpy as np
import moviepy.video.io.ImageSequenceClip
import os


def add_green_to_png(img_path, save_path):
    img = Image.open(img_path)
    img_array = np.array(img)
    print(img_array.shape)
    print(img_array[0, 0])
    green_pixel = np.array([0, 255, 0, 255])
    rows_of_pixels = 0
    number_of_pixels = 0

    for row in range(0, img_array.shape[0] - 1):
        rows_of_pixels += 1
        for col in range(0, img_array.shape[1]):
            number_of_pixels += 1
            if img_array[row, col].sum() == 0:
                img_array[row, col] = green_pixel

    data = Image.fromarray(img_array)
    data.save(save_path)


def convert_gif_to_pngs(gif_path, save_path):
    num_key_frames = 8

    with Image.open(gif_path) as im:
        for i in range(num_key_frames):
            im.seek(im.n_frames // num_key_frames * i)
            new_im = im.convert(mode=None, matrix=None, dither=None, palette='RGBA', colors=256)
            new_im.save(save_path + '{}.png'.format(i))


def convert_frames_to_video(pathIn,pathOut,fps):
    pass


