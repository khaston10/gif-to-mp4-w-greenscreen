from PIL import Image
import numpy as np
import glob
import moviepy.editor as mp
import ffmpeg
import os


def convert(gif_path):
    # Clear all old files.
    delete_all_files_in_directory("tempImages")
    delete_all_files_in_directory("greenTempImages")

    # iterate through the gifs in the folder 'gif_toConvert'.
    gif_path = gif_path
    print("Extracting PNGs from .gif.")
    convert_gif_to_pngs(gif_path, "tempImages/")

    print("Adding green screen to PNGs.")
    for filename in os.listdir("tempImages"):
        f = "tempImages/" + filename
        add_green_to_png(f, "greenTempImages/" + filename)

    print("Converting green screen pngs to new .gif.")
    convert_pngs_to_gif(gif_path)

    print("Converting .gif to MP4")
    convert_gif_to_mp4("png_to_gif.gif", gif_path)


def delete_all_files_in_directory(path_to_dir):
    for f in os.listdir(path_to_dir):
        os.remove(os.path.join(path_to_dir, f))


def add_green_to_png(img_path, save_path):
    img = Image.open(img_path)
    img_array = np.array(img)
    #print("Shape of " + str(save_path) + " is: " + str(img_array.shape))
    #print("The first pixel in this image is:               " + str(img_array[0, 0]))
    green_pixel = np.array([0, 255, 0, 255])
    rows_of_pixels = 0
    number_of_pixels = 0

    for row in range(0, img_array.shape[0] - 1):
        rows_of_pixels += 1
        for col in range(0, img_array.shape[1]):
            number_of_pixels += 1
            if img_array[row, col, 3].sum() == 0:
                img_array[row, col] = green_pixel
    #print("The pixel has been changed to:                  " + str(img_array[0, 0]))
    #print("\n")

    data = Image.fromarray(img_array)
    data.save(save_path)


def convert_gif_to_pngs(gif_path, save_path):

    with Image.open(gif_path) as im:
        num_key_frames = im.n_frames
        for i in range(num_key_frames):
            im.seek(im.n_frames // num_key_frames * i)
            new_im = im.convert(mode=None, matrix=None, dither=None, palette='RGBA', colors=256)
            new_file_name = get_new_png_file_name_given_frame_number(save_path, i, num_key_frames)
            new_im.save(new_file_name)


def get_new_png_file_name_given_frame_number(save_path, frame, total_frames):
    number_of_digits = 0
    while total_frames > 0:
        number_of_digits = number_of_digits + 1
        total_frames = total_frames // 10
    number_of_digits += 1

    new_file_index = str(frame)
    while len(new_file_index) < number_of_digits:
        # add a leading 0
        new_file_index = "0" + new_file_index

    new_file_name = save_path + new_file_index + ".png"
    return new_file_name


def get_average_duration_of_gif(gif_path):
    # returns the average duration of each frame in a gif, in 1/1000 seconds.
    avg_duration = 0
    all_duration_sum = 0
    frames = 0
    with Image.open(gif_path) as im:
        im.seek(0)
        while True:
            try:
                frames += 1
                all_duration_sum += im.info['duration']
                #print(im.info['duration'])
                im.seek(im.tell() + 1)
            except EOFError:
                #print("All Duration Sum: " + str(all_duration_sum))
                #print(frames)
                avg_duration = all_duration_sum / (frames + 1)
                return avg_duration


def convert_pngs_to_gif(original_gif_path):
    # Create the frames
    frames = []
    png_imgs = glob.glob("greenTempImages/*.png")
    for i in png_imgs:
        new_frame = Image.open(i)
        frames.append(new_frame)

    dur = get_average_duration_of_gif(original_gif_path)

    # Save into a GIF file that loops forever
    frames[0].save('png_to_gif.gif', format='GIF',
                   append_images=frames[1:],
                   save_all=True,
                   duration=dur, loop=0)


def convert_gif_to_mp4(path_to_gif, path_to_original_gif):
    average_fps = round((1 / get_average_duration_of_gif(path_to_original_gif)) * 1000)
    clip = mp.VideoFileClip(path_to_gif)
    print(clip.fps)
    print(average_fps)
    clip.write_videofile('my_video.mp4', fps=average_fps, codec='libx264', audio=False)

