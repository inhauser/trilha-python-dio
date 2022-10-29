# MÉTODO CONSTRUTOR
#O método construtor sempre é executado quando uma nova instância da classe é criada. 
# Nesse método inicializamos o estado do nosso objeto. 
# Para declarar o método construtor da classe, criamos um método com o nome __init__.

# MÉTODO DESTRUTOR
#O método destrutor sempre é executado quando uma instância (objeto) é destruída. 
# Destrutores em Python não são tão necessários quanto em C++ porque o Pyton tem um 
# coletor de lixo que lida com o gerenciamento de memória automaticamente. 
# Para declarar o método destrutor da classe, criamos um método com o nome __del__.

class Cachorro:
    def __init__(self, nome, cor, acordado=True): # nova instância da classe, método construtor __init__ (dois underline cada)
        print("Inicializando a classe...")
        self.nome = nome # atributos
        self.cor = cor
        self.acordado = acordado

    def __del__(self): # método destrutor
        print("Removendo a instância da classe.")

    def falar(self):
        print("auau")


def criar_cachorro(): # métodos fora da classe
    c = Cachorro("Zeus", "Branco e preto", False)
    print(c.nome)


c = Cachorro("Chappie", "amarelo")
c.falar()

print("Ola mundo")

del c # palavra reservada del, faz as vezes de destrutor, limpando a base com relaçao ao objeto neste ponto do código.

print("Ola mundo")
print("Ola mundo")
print("Ola mundo")

# criar_cachorro()
