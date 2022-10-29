# Parâmetros podem ser passados por posição, por posição e nome, ou por nome.
# def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
#       positional only => positional or keyword => keyword only
# Neste caso, exploraremos apenas a keyword only, "nomeados", excluindo as duas primeiras.

def criar_carro(*, modelo, ano, placa, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")  # válido

# criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")
# inválido, pois somente pode admitir nomeado, em virtude do *, na função; e os 3 primeiro itens estão apenas com posição.
