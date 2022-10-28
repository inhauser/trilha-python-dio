# elimina os objetos duplicados dentro de um elemento iterável.
# set não garante a ordem, não confiar na ordem, pode não estar ordenado.
# ao invés de escrever set posso substituir por chaves {}

numeros = set([1, 2, 3, 1, 3, 4])
print(numeros)  # {1, 2, 3, 4}

letras = set("abacaxi")
print(letras)  # {"b", "a", "c", "x", "i"}

carros = set(("palio", "gol", "celta", "palio"))
print(carros)  # {"gol", "celta", "palio"}

linguagens = {"python", "java", "python"}
print(linguagens)
