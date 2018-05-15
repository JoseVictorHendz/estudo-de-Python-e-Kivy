#coding: utf-8
from kivy.app import App
from kivy.uix.label import Label


def build():
    return Label(text = 'hello world')

hello_horld = App()
hello_horld.build = build
hello_horld.run()