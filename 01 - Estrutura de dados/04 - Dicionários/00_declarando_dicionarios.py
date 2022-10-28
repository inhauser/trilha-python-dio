# chave:valor - apenas a chave tem que ser imutável e pode ser, por ex, tupla. valor pode ser qquer tipo de objeto, e pode ser alterado. 
#Chave valor único. Dict (:) ou {:}
# para recuperar valor, faço a chamada plea chave.

pessoa = {"nome": "Guilherme", "idade": 28}
print(pessoa)

pessoa = dict(nome="Guilherme", idade=28)
print(pessoa)

pessoa["telefone"] = "3333-1234"  # {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}
print(pessoa)
