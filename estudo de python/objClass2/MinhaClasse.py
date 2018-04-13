class MinhaClasse:
    membro_cls =50
    def __init__(self):
        self.membro_inst = -10
    def func(self):
        print(self.membro_inst)
        print(self.membro_cls)
        print(MinhaClasse.membro_cls)

instancia1 = MinhaClasse()
instancia2 = MinhaClasse()
print(MinhaClasse.membro_cls)
print(instancia1.membro_cls, instancia2.membro_cls)




# instancia1.membro_inst = 10
# print(instancia1.membro_inst)
# print(instancia2.membro_inst)
