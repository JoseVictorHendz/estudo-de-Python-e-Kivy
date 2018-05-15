import kivy
kivy.require("1.9.1")
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class MinhaTela(BoxLayout):
    def mensagem(self):
       ti = self.ids.text_input = ""
       print("-----",ti)
class Estudo1App(App):
    pass


janela = Estudo1App()
janela.run()