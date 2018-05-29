'''
Basic camera example
Default picture is saved as
/sdcard/org.test.cameraexample/enter_file_name_here.jpg
'''

from os import getcwd
from os.path import exists
from os.path import splitext

import kivy
kivy.require('1.8.0')

from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.logger import Logger

from plyer import camera


class CameraDemo(FloatLayout):
    def __init__(self):
        super(CameraDemo, self).__init__()
        self.cwd = getcwd() + "/"
        # self.ids.path_label.text = self.cwd

    def tirarFoto(self):
        filepath = self.cwd + self.ids.filename_text.text
        ext = splitext(filepath)[-1].lower()

        if(exists(filepath)):
            popup = MsgPopup("Ja existe uma foto com este nome!")
            popup.open()
            return False

        try:
            camera.take_picture(filename=filepath,
                                on_complete=self.retornoCamera)
        except NotImplementedError:
            popup = MsgPopup(
                "nao tem suporte para esta plataforma")
            popup.open()

    def retornoCamera(self, filepath):
        if(exists(filepath)):
            popup = MsgPopup("Foto salva!")
            popup.open()
        else:
            popup = MsgPopup("nao foi possivel salvar")
            popup.open()


class CameraDemoApp(App):
    def __init__(self):
        super(CameraDemoApp, self).__init__()
        self.demo = None

    def build(self):
        self.demo = CameraDemo()
        return self.demo

    def on_pause(self):
        return True

    def on_resume(self):
        pass


class MsgPopup(Popup):
    def __init__(self, msg):
        super(MsgPopup, self).__init__()
        self.ids.menssagem.text = msg


if __name__ == '__main__':
    CameraDemoApp().run()