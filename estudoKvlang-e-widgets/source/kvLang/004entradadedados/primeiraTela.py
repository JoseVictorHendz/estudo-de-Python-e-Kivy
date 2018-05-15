from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

def click():
    print(ed.text)

def build():
    layout = FloatLayout()
    global ed
    ed = TextInput(text='eXcript')

    ed.size_hint = None, None
    ed.height = 300
    ed.width =400
    ed.x = 60
    ed.y = 250

    bt = Button(text='click aqui')
    bt.size_hint = None, None
    ed.height = 50
    ed.width = 200
    ed.y = 150
    ed.x = 170

    layout.add_widget(ed)
    layout.add_widget(bt)


    # bt.on_press = click

    return layout


janela = App()

from kivy.core.window import Window
Window.size = 600, 600
janela.title = 'eXcript'

janela.build = build
janela.run()