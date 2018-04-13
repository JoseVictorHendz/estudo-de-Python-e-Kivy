from kivy.app import App
from kivy.core.window import Window
from  kivy.utils import get_color_from_hex as c
# Window.clearcolor = [1, 1, 1, 1]
Window.clearcolor = c("#FFFFFF")
class Estudo1App(App):
    pass

janela = Estudo1App()
janela.run()