# Método
# Cria chaves. 1- qdo quer apenas criar chave, sem valor. 2- criar conjunto de chaves com valor único.

resultado = dict.fromkeys(["nome", "telefone"])  # {"nome": None, "telefone": None}
print(resultado)

resultado = dict.fromkeys(["nome", "telefone"], "vazio")  # {"nome": "vazio", "telefone": "vazio"}
print(resultado)
