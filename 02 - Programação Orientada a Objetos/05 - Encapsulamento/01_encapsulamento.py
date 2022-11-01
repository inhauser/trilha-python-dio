#O encapsulamento é um dos conceitos fundamentais em programação orientada a objetos. 
# Ele descreve a ideia de agrupar dados e os métodos que manipulam esses dados em uma unidade. 
# Isso impõe restrições ao acesso direto a variáveis ​​e métodos e pode evitar a modificação acidental de dados. 
# Para evitar alterações acidentais, a variável de um objeto só pode ser alterada pelo método desse objeto.
# em diagrama sinal de - informa que é privado - só pode ser acessado pela classe: ex. saldo.
# em diagrama sinal de + informa que é público - pode ser acessado fora da classe: ex: cliente depositar e sacar.
# Convenções nome: _nome é privado.
# Todos os recursos são públicos, a menos que o nome inicie com underline. 
# Ou seja, o interpretador Python não irá garantir a proteção do recurso, mas por ser uma convenção amplamente adotada na comunidade, 
# quando encontramos uma variável e/ou método com nome iniciado por underline, sabemos que não deveríamos manipular o seu valor diretamente, 
# ou invocar o método fora do escopo da classe.


class Conta:
    def __init__(self, nro_agencia, saldo=0):
        self._saldo = saldo
        self.nro_agencia = nro_agencia

    def depositar(self, valor):
        # ...
        self._saldo += valor

    def sacar(self, valor):
        # ...
        self._saldo -= valor

    def mostrar_saldo(self):
        # ...
        return self._saldo


conta = Conta("0001", 100)
conta.depositar(100)
print(conta.nro_agencia)
print(conta.mostrar_saldo())
