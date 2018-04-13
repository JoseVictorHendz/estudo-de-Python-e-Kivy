#coding: utf-8
class Retangulo:
    def __init__(self, largura, altura):
       self._largura = 0
       self._altura  = 0
       self.largura = largura
       self.altura = altura

    @property
    def altura(self):
        print('get altura')
        return self._altura
    @altura.setter
    def altura(self, value):
        if (not (isinstance(value, int) and value > 0)):
            raise ValueError('Largura invalida: {}'.format(value))
        self._altura = value
    @property
    def largura(self):
        print(('getlargura'))
        return self._largura
    @largura.setter
    def largura(self, value):
        if (not (isinstance(value, int) and value > 0)):
            raise ValueError('Largura invalida: {}'.format(value))
        self._largura = value
    @property
    def area(self):
        return self._altura * self._largura

    # altura = property(fget=get_altura, fset=_set_altura)
    # largura = property(fget=get_largura, fset=_set_altura)
    # area = property(fget=_get_area)

retangulo = Retangulo(largura=5, altura=5)

retangulo.altura = 15
retangulo.largura = 20
print("altura é {} e a largura é {} a area fica {}".format(retangulo.altura, retangulo.largura, retangulo.area))

