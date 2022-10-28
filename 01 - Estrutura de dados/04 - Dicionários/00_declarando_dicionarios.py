# chave:valor - chave tem ques er imutável e pode ser, por ex, tupla. valor pode ser qquer tipo de objeto. Chave valor único. Dict (:) ou {:}
# para recuperar valor, faço a chamada plea chave.

pessoa = {"nome": "Guilherme", "idade": 28}
print(pessoa)

pessoa = dict(nome="Guilherme", idade=28)
print(pessoa)

pessoa["telefone"] = "3333-1234"  # {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}
print(pessoa)
