# MÉTODOS DE CLASSE
#Métodos de classe estão ligados à classe e não ao objeto. 
# Eles têm acesso ao estado da classe, pois recebem um parâmetro que aponta para a classe e não para a instância do objeto.

# MÉTODOS ESTÁTICOS
# Um método estático não recebe um primeiro argumento explícito. 
# Ele também é um método vinculado à classe e não ao objeto da classe. 
# Este método não pode acessar ou modificar o estado da classe. 
# Ele está presente em uma classe porque faz sentido que o método esteja presente na classe.

# MÉTODOS DE CLASSE X MÉTODOS ESTÁTICOS
# Um método de classe recebe um primeiro parâmetro que aponta para a classe, enquanto um método estático não.
# Um método de classe pode acessar ou modificar o estado da classe enquanto um método estático não pode acessá-lo ou modificá-lo.

# Quando utilizar método de classe ou estático
# Geralmente usamos o método de classe para criar métodos de fábrica, que são métodos que retornam instâncias da classe.
# Geralmente usamos métodos estáticos para criar funções utilitárias. Exemplo, dentro da classe pessoa, para validar se é maior de idade.

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2022 - ano
        return cls(nome, idade)

    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18


p = Pessoa.criar_de_data_nascimento(1994, 3, 21, "Guilherme")
print(p.nome, p.idade)

print(Pessoa.e_maior_idade(18))
print(Pessoa.e_maior_idade(8))
