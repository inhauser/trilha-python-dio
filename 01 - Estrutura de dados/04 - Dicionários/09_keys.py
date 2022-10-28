# Método
# Retorna somente as chaves de um dicionário
# Útil para saber quais as chaves que o dicionário tem.

contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

resultado = contatos.keys()  # dict_keys(['guilherme@gmail.com'])
print(resultado)

novo_dicionario = {"a": 100, 1: "teste", "b": "python"}
print(novo_dicionario.keys())
