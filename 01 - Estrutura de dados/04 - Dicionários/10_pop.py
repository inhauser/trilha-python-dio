# Método
# Para remover um valor.
# Retorna o valor que removeu.
# Podemos atribuir um valor para retornar se não encontrada.

contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

resultado = contatos.pop("guilherme@gmail.com")  # {'nome': 'Guilherme', 'telefone': '3333-2221'}
print(resultado)

resultado = contatos.pop("guilherme@gmail.com", {})  # {}
print(resultado)
