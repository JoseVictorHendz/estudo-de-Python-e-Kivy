from kivy.app import App
from kivy.uix.textinput import TextInput

def build():
    return TextInput(text='componente Text input')

janela = App()
janela.build = build
janela.run()