from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
import os
from imageFunctions import *
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty
import Global

green_screen_color = "GREEN"
directory_home = "K:\\Users\\kevoh"

# Designate our .kv file
Builder.load_file('gif_to_mp4.kv')


class MyLayout(Widget):

    def check_box(self, instance, value, color):
        Global.green_screen_color = color
        self.ids.feedback.text = "Green screen color has been set to " + color
        print(Global.green_screen_color)

    def convert(self):
        if self.ids.feedback.text[-4:] == ".gif":
            self.ids.feedback.text = "Converting is in progress... Please wait."
            path_to_gif = self.ids.filechooser.selection[0]
            path_for_save = os.path.split(path_to_gif)[0] + "\\"
            convert(path_to_gif, path_for_save)
            self.ids.filechooser._update_files()

        else:
            self.ids.feedback.text = "No gif has been selected."

    def get_file_path(self, file_name):
        try:
            self.ids.feedback.text = "Path: " + file_name[0]
        except:
            self.ids.feedback.text = "Path: No .gif File Selected"

    def set_home_directory(self):
        self.ids.feedback.text = "Home directory has been set."
        Global.write_new_directory_path(self.ids.filechooser.path)

    def load_home_directory_on_start(self):
        self.ids.feedback.text = ""
        return Global.get_directory_path()


class GifToVideoApp(App):
    def __init__(self, **kwargs):
        super().__init__()

    def build(self):
        Window.clearcolor = (.3, .3, .3, 1)
        #self.load_home_directory_on_start(MyLayout())
        return MyLayout()


if __name__ == '__main__':
    GifToVideoApp().run()
