import kivy
kivy.require("1.9.1")
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class MinhaTela(BoxLayout):
    def click(self):
        print('top de mais')
        self.ids.lbl1.text = ""
        self.ids.lbl2.text = "10"

class EstudApp(App):
    pass


janela = EstudApp()
janela.run()