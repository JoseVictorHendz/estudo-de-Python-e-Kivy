


listaNum = [100, 200, 300, 400]
listaNum.reverse()  # inverte a lista
print('count', listaNum.count(10))  # conta quantas vezes o parametro aparece no array
listaNum.append(1000)  # adiciona no final
print('index', listaNum.index(1000))  # retorna o index
print(listaNum)
print('---------------------')
t = tuple('abc')
print(t)
print('---------------------')
d = dict()  # diciona é tipo um json, funcoes para ele: del, keys, values,
# popitem, dicionario.update(dicionario1)

d['abc'] = 100
d['def'] = 1000
d['ghi'] = 10000
print(d)


def retorna():
    return 1, 2

def paramLisra(*lista):
    print(lista)

def paramDicionario(**dicionario):
    print(dicionario)

def argumentos(*args, **kwargs):
    print(args)
    print(kwargs)

a1, b2 = retorna()  # retorno multiplo

paramLisra("oi", "eae")

paramDicionario(a=1, b=2, c=3)

argumentos(1, 2, 3, 4, um=1, dois=2, tres=3, quatro=4)

# try cach
def erro(x):
    try:
        eval(x)
    except TypeError:
        print('typeError')
    except NameError:
        print('typeError')
    except ValueError:
        print('valueErroe')
    except ValueError:
        print('valueError')
    except ZeroDivisionError:
        print('ZeroDivisionError')
    else: print('nao se perdeu na malandragem')

    finally: print('sempre é executado\n')


erro("int+int")
erro("a")
erro("int('a')")
erro("10/0")