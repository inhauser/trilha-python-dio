# Podemos combinar parâmetros obrigatórios com args e kwargs (nomes por convenção, mas podem ser outros que desejarmos.
# Quando definidos, o método recebe os valores como tupla e dicionário respectivamente.

def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()]) #.join para concatennar. .items por ser dicionário.
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)


exibir_poema(
    "Sexta-feira, 26 de agosto de 2022", # primeiro item da função; considera data_extenso
    "Zen of Python", # Args acima como texto - inserção como tuplas no padrão "", e enter sucessivamente até terminar args e começar kwargs (dicionário)
    "Beautiful is better than ugly.",
    "Explicit is better than implicit.",
    "Simple is better than complex.",
    "Complex is better than complicated.",
    "Flat is better than nested.",
    "Sparse is better than dense.",
    "Readability counts.",
    "Special cases aren't special enough to break the rules.",
    "Although practicality beats purity.",
    "Errors should never pass silently.",
    "Unless explicitly silenced.",
    "In the face of ambiguity, refuse the temptation to guess.",
    "There should be one-- and preferably only one --obvious way to do it.",
    "Although that way may not be obvious at first unless you're Dutch.",
    "Now is better than never.",
    "Although never is often better than *right* now.",
    "If the implementation is hard to explain, it's a bad idea.",
    "If the implementation is easy to explain, it may be a good idea.",
    "Namespaces are one honking great idea -- let's do more of those!",
    autor="Tim Peters", # quando termina a inbserção por tuplas "", , reconhece que não é mais args. Iniciados kwargs, aciam como meta_dados, 
    #e fazemos a inserção chave:valor do dicionário.
    ano=1999,
)
