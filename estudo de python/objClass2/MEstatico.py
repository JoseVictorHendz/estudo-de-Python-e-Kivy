class Mestatico:
    @staticmethod
    def func1():
        print('func1()')
    @staticmethod
    def func2(x, y):
        print("funcao '{}' invocada.\nParams=({}{})".format('func2', x, y))
    @staticmethod
    def func3(a, b, c):
        info = """
        Nome da funcao: {nome}
        quantidade de args: {quantidade}
        args: {args}
        """
        info = info.format(nome=Mestatico.func3.__name__,
                    quantidade=Mestatico.func3.__code__.co_argcount,
                    args = Mestatico.func3.__code__.co_varnames)
        print(info)
me = Mestatico
me.func1()
me.func2(100,200)
me.func3(5,10,15)
