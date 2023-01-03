green_screen_color = "GREEN"


def write_new_directory_path(directory_home):
    f = open("home_directory.txt", "w")
    f.write(directory_home)
    f.close()


def get_directory_path():
    # open and read the file after the appending:
    f = open("home_directory.txt", "r")
    return f.read()

