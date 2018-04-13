from kivy.app import App
from kivy.uix.button import Button
def click():
    print('top da balada ate clica clicou')
def build():
    bt = Button(text="Clique aqui")
    bt.on_press = click
    return bt
janela = App()
janela.build = build
janela.run()