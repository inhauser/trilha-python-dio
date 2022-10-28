# Conjuntos em python não suportam indexação e nem fatiamento, sendo necessário converter o conjunto/set para lista.

numeros = {1, 2, 3, 2}

numeros = list(numeros)

print(numeros[0])
