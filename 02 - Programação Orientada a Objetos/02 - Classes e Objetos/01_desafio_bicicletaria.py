# João tem uma bicicletaria e gostaria de registrar as vendas de suas bicicletas. 
# Crie um programa onde João informe: cor, modelo, ano e valor da bicicleta vendida. 
# Uma bicicleta pode: buzinar, parar e correr. 
# Adicione esses comportamentos!

# self é uma referência explícita para o objeto; queremos dizer que essa é a instância do objeto; 
# poderia chamar de this, mas a convenção é chamar self.


class Bicicleta:
    def __init__(self, cor, modelo, ano, valor): # método construtor
        # pass - se quisesse deixar vazio
        self.cor = cor # atributos da classe
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self): # método / comportamento. Métodos são funções dentro de uma classe.
        # diferença em método é que deve passar um primeiro argumento que chama self.
        print("Plim plim...")

    def parar(self):
        print("Parando bicicleta...")
        print("Bicicleta parada!")

    def correr(self):
        print("Vrummmmm...")

    #def get_cor(self):
     #   return(self.cor)
    # erro comum é esquecer o self, o argumento do método, conteha ele valor ou não.

    def __str__(self): # método para retornar a exibição da instância de uma forma mais amigável (vide print (b2) abaixo)
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}" # dinâmico
        #return f"Bicicleta: cor={self.cor}, modelo={self.modelo}, ano={self.ano}, valor={self.valor}" # hard coded.


b1 = Bicicleta("vermelha", "caloi", 2022, 600) # objeto instanciado
b1.buzinar()
b1.correr()
b1.parar()
print(b1.cor, b1.modelo, b1.ano, b1.valor)

b2 = Bicicleta("verde", "monark", 2000, 189)
#b2.buzinar() # Bicicleta.buzinar(b2)
print(b2) # exibir instância
b2.correr()
#b2.cor()
#print(b2.get_cor())
