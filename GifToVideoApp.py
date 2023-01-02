from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
import os
from imageFunctions import *
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty

green_screen_color = "GREEN"

# Designate our .kv file
Builder.load_file('gif_to_mp4.kv')


class MyLayout(Widget):

    def check_box(self, instance, value, color):
        green_screen_color = color

    def convert(self):
        if self.ids.path.text[-4:] == ".gif":
            self.ids.feedback.text = "Converting is in progress... Please wait."
            path_to_gif = self.ids.path.text[6:]
            path_for_save = os.path.split(path_to_gif)[0] + "\\"
            print(path_for_save)
            convert(path_to_gif)

        else:
            self.ids.feedback.text = "No gif has been selected."

    def get_file_path(self, file_name):
        try:
            self.ids.path.text = "Path: " + file_name[0]
        except:
            self.ids.path.text = "Path: No File Selected"


class GifToVideoApp(App):
    def build(self):
        return MyLayout()


if __name__ == '__main__':
    GifToVideoApp().run()