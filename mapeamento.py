from exudemy25 import produtos, pessoas, lista

#nova_lista = list(map(lambda x: x * 2, lista))
# nova_lista = [x * 2 for x in lista]
# print(lista)
# print(nova_lista)

# def aumenta_preco(p):
#     p['preco'] = round(p['preco'] * 1.05, 2)
#     return p
#
# novos_produtos = map(aumenta_preco, produtos)
#
# for produto in novos_produtos:
#     print(produto)
#
# nomes = map(lambda p: p['nome'] * 1.20, pessoas)
#
# for p in nomes:
#     print(p)

#---------------------------------------------------------------------------------------------------
def filtra(pessoa):
    if pessoa['idade'] >= 18:
        return True
    else:
        return False

nova_lista = filter(filtra, pessoas)

for produto in nova_lista:
    print(produto)
