# ao invés de utilizar o append, que permite a adição de apenas um item à lista, utilizo extend para adicionar diversos itens.
# se eu repetir o item, ele ficará duplicado na lista

linguagens = ["python", "js", "c"]

print(linguagens)  # ["python", "js", "c"]

linguagens.extend(["java", "csharp"])

print(linguagens)  # ["python", "js", "c", "java", "csharp"]
