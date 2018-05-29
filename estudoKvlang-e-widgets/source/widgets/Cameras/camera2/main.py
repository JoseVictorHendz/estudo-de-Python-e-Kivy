from kivy.lang import Builder
from kivy.app import App
from kivy.clock import Clock
from plyer import camera

class MyApp(App):
    count = 0

    def build(self):
        import pygame
        print 'pygame version:', pygame.ver
        print 'SDL version:', pygame.get_sdl_version()

    def on_pause(self):
        print 'on_pause'
        return True

    def on_resume(self):
        print 'on_resume'

    def tirar_foto(self):
        print 'tirando foto...'
        filename = '/sdcard/foo.jpg'
        camera.take_picture(str(filename), self.foto_tirada)

    def foto_tirada(self, filename):
        print 'foto tirada', filename

if __name__ == '__main__':
    MyApp().run()