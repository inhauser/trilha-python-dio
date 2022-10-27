# como a lista é mutável, se eu copiar a lista, ela pode ser mantida na lista originária, ou na lista copiada, permitindo alterações dissociadas.
# o id permite identificar que se tratam de listas diferentes

lista = [1, "Python", [40, 30, 20]]

lista.copy()

print(lista)  # [1, "Python", [40, 30, 20]]

l2 = lista.copy()

print(id(l2), id(lista))

l2[0] = 2

print(l2)

print(lista)
