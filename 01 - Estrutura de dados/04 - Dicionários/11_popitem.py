# Método
# Difrença para o pop é que aqui não informa a chave, e vai retirando itens na sequência.
# Se estiver vazio retorna erro / exceção.

contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

resultado = contatos.popitem()  # ('guilherme@gmail.com', {'nome': 'Guilherme', 'telefone': '3333-2221'})
print(resultado)

# contatos.popitem()  # KeyError
