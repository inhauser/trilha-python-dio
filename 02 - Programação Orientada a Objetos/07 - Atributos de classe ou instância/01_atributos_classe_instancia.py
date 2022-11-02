# ATRIBUTOS DO OBJETO
# Todos os objetos nascem com o mesmo número de atributos de classe e de instância. 
# Atributos de instância são diferentes para cada objeto (cada objeto tem uma cópia), 
# já os atributos de classe são compartilhados entre os objetos.

class Estudante:
    escola = "DIO"

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self) -> str:
        return f"{self.nome} - {self.matricula} - {self.escola}"


def mostrar_valores(*objs):
    for obj in objs:
        print(obj)


aluno_1 = Estudante("Guilherme", 1)
aluno_2 = Estudante("Giovanna", 2)
mostrar_valores(aluno_1, aluno_2)

Estudante.escola = "Python" # quando altero instância ela afeta todos os objetos.
aluno_1 = Estudante("Guilherme", 4) # quando altero objeto os outros objetos não são afetados.
aluno_3 = Estudante("Chappie", 3) 
mostrar_valores(aluno_1, aluno_2, aluno_3)
