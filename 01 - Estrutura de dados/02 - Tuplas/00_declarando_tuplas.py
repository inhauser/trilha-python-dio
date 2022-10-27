# Tuplas: imutáveis, bem mais restritas. Listas: mutáveis.
# É de boa prática colocar vírgula no final. Isso evita que o python confunda a tupla com uma ordem de precedência entre parênteses (se não for utilizado tuple).
# uma tupla pode conter uma lista dentro dela, como no exemplo numérico abaixo. Todos os tipos de objeto, inclusive tuplas aninhadas.
# utiliza-se o colchete e o valor do índice, da mesma forma que se faz na lista, inclusive os negativos - slice

frutas = (
    "laranja",
    "pera",
    "uva",
)
print(frutas)

letras = tuple("python")
print(letras)

numeros = tuple([1, 2, 3, 4])
print(numeros)

pais = ("Brasil",)
print(pais)

matriz = (
    (1, "a", 2),
    ("b", 3, 4),
    (6, 5, "c"),
)

matriz[0] # (1, "a", 2)
matriz[0][0] # 1
matriz[0][-1] # 2
matriz[-1][-1] # "c"

# fatiamento / slicing

tupla = ("p", "y", "t", "h", "o", "n",)

tupla[2:] # ("t", "h", "o", "n")
tupla[:2] # ("p", "y")
tupla[1:3] # ("y", "t")
tupla[0:3:2] # ("p", "t")
tupla[::] # ("p", "y", "t", "h", "o", "n")
tupla[::-1] # ("n", "o", "h", "t", "y", "p")
