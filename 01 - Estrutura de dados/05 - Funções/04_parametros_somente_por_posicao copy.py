# Parâmetros podem ser passados por posição, por posição e nome, ou por nome.
# def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
#       positional only => positional or keyword => keyword only
# Neste caso, exploraremos as duas primerias hipóteses, excluindo a keyword only

def criar_carro(modelo, ano, placa, /, marca, motor, combustivel): # antes de /, modelo ano e placa: somente por posição; após /, pode ser nome ou posição. 
    print(modelo, ano, placa, marca, motor, combustivel)


criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")
#válido, pois passa o três primeiros itens posicionados, e os três últimos nomeados.

criar_carro("Palio", 1999, "ABC-1234", "Fiat", "1.0", "Gasolina")
# também é válido, pois com a / na função, depois dos três primeiros itens por ser posição ou nomeado.

#criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")
# inválido, pois tentou passar nomeado as três primeiras posições.
