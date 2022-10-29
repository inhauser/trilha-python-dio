# return para retornar um valor. Em Python, padrão retorna None. Uma função pode retornar mais de um valor.

def calcular_total(numeros):
    return sum(numeros)


def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor

def fun_3():
    print("Olá mundo!")
    # return None - se eu omitir, por padrão retornará None, então não é necessário declarar.


print(calcular_total([10, 20, 34]))  # 64
print(retorna_antecessor_e_sucessor(10))  # (9, 11)
