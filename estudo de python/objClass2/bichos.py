
class Bicho:
    qtd_bichos = 0
    def __init__(self):
        self.add_bicho()
    def __del__(self):
        self.del_bicho()
        if self.qtd_bichos == 0:
            print("todos morreram")
    @classmethod
    def add_bicho(cls):
        cls.qtd_bichos += 1
    @classmethod
    def del_bicho(cls):
        cls.qtd_bichos -= 1


bicho1 = Bicho()
print('-------', Bicho.qtd_bichos)
bicho2 = Bicho()
print('-------', Bicho.qtd_bichos)
bicho3 = Bicho()
print('-------', Bicho.qtd_bichos)

del(bicho1)
print('----', Bicho.qtd_bichos)
del(bicho2)
print('----', Bicho.qtd_bichos)
del(bicho3)
print('----', Bicho.qtd_bichos)

