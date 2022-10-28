# Método
# Outra forma de acessar dadosd e um dicionário.
# Se chamar uma chave inexistente não retorna exceção/erro (key error)
# Se não tenho certeza se uma chave existe ou não, uso get. Se não existir retorna None.
# Posso também atribuir um valor se não encontrar, como, por exemplo, retornar vazio.

contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

# contatos["chave"]  # KeyError

resultado = contatos.get("chave")  # None
print(resultado)

resultado = contatos.get("chave", {})  # {}
print(resultado)

resultado = contatos.get(
    "guilherme@gmail.com", {}
)  # {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
print(resultado)
