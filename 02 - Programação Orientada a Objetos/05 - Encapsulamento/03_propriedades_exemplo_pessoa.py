class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self.nome = nome
        self._ano_nascimento = ano_nascimento

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        _ano_atual = 2022
        return _ano_atual - self._ano_nascimento

    # def get_nome(self): mais comum em Java e C++
        return self._nome
    
    # def get_idade(self): mais comum em Java e C++
        return 2022 - self._ano_nascimento

pessoa = Pessoa("Guilherme", 1994)
print(f"Nome: {pessoa.nome} \tIdade: {pessoa.idade}")
# print(f"NOme: {pessoa.get_nome()} \tIdade: {pessoa.get_idade()}")
