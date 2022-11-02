# A palavra polimorfismo significa ter muitas formas. 
# Na programação, polimorfismo significa o mesmo nome de função (mas assinaturas diferentes) sendo usado para tipos diferentes.
# A função len é um exemplo. Se passo sting conta número de caracteres da string. 
# Se passo lista numérica, ele retorna quantos itens tem dentro da lista

# Na herança, a classe filha herda os métodos da classe pai. 
# No entanto, é possível modificar um método em uma classe filha herdada da classe pai. 
# Isso é particularmente útil nos casos em que o método herdado da classe pai não se encaixa perfeitamente na classe filha.


class Passaro:
    def voar(self):
        print("Voando...")


class Pardal(Passaro):
    def voar(self):
        # super().voar()
        print("Pardal pode voar")


class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não pode voar")




# NOTE: exemplo ruim do uso de herança para "ganhar" o método voar
class Aviao(Passaro):
    def voar(self):
        print("Avião está decolando...")


def plano_voo(obj): # não interessa o objeto pardal, avstruz, etc..., eu quero retornar quem possua o método voar.
    obj.voar()      # o polimorfismo evita ter que criar plano_voo_pardal, plano_voo_avestruz, plano_voo_avião.

# p1 = Pardal()
# p2 = Avestruz()

# plano_voo(p1)
# plano_voo(p2)

plano_voo(Pardal())
plano_voo(Avestruz())
plano_voo(Aviao())
