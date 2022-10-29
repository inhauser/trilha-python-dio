# Python trabalha com escopolo local e global.
# Dentro do bloco da função o escopo é local. Assim as alterações alí feitas em objetos imutáveis serão perdiadas quando o método terminar de ser executado.
# Para usar objetos globais usa-se a palavra-chave global, que informa ao interpretador que a variável que está sendo manipulada no escopo local é global.
# Utiliza-se para quando quero pegar um valor/argumento que está global e não na esfera local.
# NÃO É BOA PRÁTICA E DEVE SER EVITADA.

salario = 2000 # variável fora do escopo local. é global, porque está fora da função. Está na raiz do programa.

#def salario_bonus(bonus): 
    #salario += bonus
    #return salario
# essa função acima retorna erro: "local variable salario referenced before assignment"

def salario_bonus(bonus): # escopo local
    global salario
    salario += bonus
    return salario


salario_com_bonus = salario_bonus(500)  # 2500
print(salario_com_bonus)


############################# outro exemplo
salario = 2000 # variável fora do escopo local. é global, porque está fora da função. Está na raiz do programa.

def salario_bonus(bonus, lista): # escopo local
    global salario
    #lista.append(2)
    lista_aux = lista.copy()
    lista_aux.append(2)
    print(f"lista aux={lista_aux}")
    salario += bonus
    return salario

lista = [1]
salario_com_bonus = salario_bonus(500, lista)  # 2500
print(salario_com_bonus)
#print(lista) # retorna [1 , 2]
print(lista) # retorna [1]
