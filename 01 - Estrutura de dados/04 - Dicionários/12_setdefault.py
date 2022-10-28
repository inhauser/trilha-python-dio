# Método
# Muito utilizado no dia-a-dia
# Se o atributo não estiver não estiver no dicionário, adiciona o atributo com o valor que inseri no código.
# SE o atributo estiver no dicionário, ele retorna o valor do dicionário e não altera ele.
# Útil para o caso de se precisar um valor caso ele não exista, sem ter que fazer essa verificação antes. E preserva o valor se já existente, sem sobrescrever.

contato = {"nome": "Guilherme", "telefone": "3333-2221"}

contato.setdefault("nome", "Giovanna")  # "Guilherme"
print(contato)  # {'nome': 'Guilherme', 'telefone': '3333-2221'}

contato.setdefault("idade", 28)  # 28
print(contato)  # {'nome': 'Guilherme', 'telefone': '3333-2221', 'idade': 28}
