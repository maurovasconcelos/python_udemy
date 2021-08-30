"""
Treinando tratamento de erro
"""

def covnerte_numero(valor):
    try:
        valor = int(valor)
        return valor
    except ValueError:
        try:
            valor = float(valor)
            return valor
        except ValueError:
            pass

while True:
    numero = covnerte_numero(input('Digite um número: '))

    if numero is None:
        print('Erro: Isso não é um numero')
    else:
        print(numero * 2)