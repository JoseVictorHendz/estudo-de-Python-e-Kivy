from kivy.lang import Builder
from kivy.app import App
from kivy.clock import Clock
from plyer import camera

kv = """
BoxLayout:
    orientation: 'vertical'
    Button:
        text: 'reconhecer um objeto'
        on_release: app.tirar_foto()

    Button:
        text: 'Sair do aplicativo'
        on_release: app.stop()
"""

class MyApp(App):
    count = 0

    def build(self):
        import pygame
        print 'pygame version:', pygame.ver
        print 'SDL version:', pygame.get_sdl_version()
        return Builder.load_string(kv)

    def on_pause(self):
        print 'on_pause'
        return True

    def on_resume(self):
        print 'on_resume'

    def tirar_foto(self):
        print 'taking pic...'
        filename = '/sdcard/foo.jpg'
        camera.take_picture(str(filename), self.picture_taken)

    def picture_taken(self, filename):
        print 'pic taken', filename

if __name__ == '__main__':
    MyApp().run()