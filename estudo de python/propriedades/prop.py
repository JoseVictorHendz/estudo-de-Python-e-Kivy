#coding: utf-8
__author__ = "jose"

class Classeteste:
    def __init__(self):
        self._varPrivada = 10
    @property
    def x(self):
        print('get top')
        return self._varPrivada
    @x.setter
    def x(self, value):
        print('set top')
        self._varPrivada = value

    # var = property(fget=_get_var, fset=_set_var)


testeObjeto = Classeteste()
testeObjeto.x = 10
t = testeObjeto.x
