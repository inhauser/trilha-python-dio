# João tem uma bicicletaria e gostaria de registrar as vendas de suas bicicletas. 
# Crie um programa onde João informe: cor, modelo, ano e valor da bicicleta vendida. 
# Uma bicicleta pode: buzinar, parar e correr. 
# Adicione esses comportamentos!

# self é uma referência explícita para o objeto; queremos dizer que essa é a instância do objeto; poderia chamar de this, mas a convenção é chamar self.

class Bicicleta:
    def __init__(self, cor, modelo, ano, valor): # método construtor
        # pass se quiser deixar em branco.
        self.cor = cor # atributos da classe
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        
b1

    def buzinar(self):
        print("Plim plim...")

    def parar(self):
        print("Parando bicicleta...")
        print("Bicicleta parada!")

    def correr(self):
        print("Vrummmmm...")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


b1 = Bicicleta("vermelha", "caloi", 2022, 600) # objeto instanciado
b1.buzinar()
b1.correr()
b1.parar()
print(b1.cor, b1.modelo, b1.ano, b1.valor)

b2 = Bicicleta("verde", "monark", 2000, 189)
print(b2)
b2.correr()
