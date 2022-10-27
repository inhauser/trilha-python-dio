# built-in sorte, função.
# Funciona como o sort, porém é uma função e a sintaxe é específica, diferindo daquela do sort.

linguagens = ["python", "js", "c", "java", "csharp"]

print(sorted(linguagens, key=lambda x: len(x)))  # ["c", "js", "java", "python", "csharp"]
print(sorted(linguagens, key=lambda x: len(x), reverse=True))  # ["python", "csharp", "java", "js", "c"]

print(sorted(linguagens))
