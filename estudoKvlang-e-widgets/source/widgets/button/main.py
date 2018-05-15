import kivy
kivy.require("1.9.1")
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class MinhaTela(BoxLayout):
    def click(self):
        print('top de mais')
        self.ids.btn1.text = "on press"
    def fim_click(self):
        self.ids.btn1.text = "on realese"

class Estudo1App(App):
    pass


janela = Estudo1App()
janela.run()