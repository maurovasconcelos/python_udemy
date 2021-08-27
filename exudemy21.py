"""
Some os valores nas listas retornando uma nova lista com os valores somados:

Se uma lista for maior que a outra, a soma só vai consederar o tamanho da menor.

Exemplo:
lista_a     = [1,2,3,4,5,6,7]
lista_b     = [1,2,3,4]

=============== resultado
lista_soma  = [2,4,6,8]
"""

lista_a = [1,2,3,4,5,6,7]
lista_b = [1,2,3,4]

# lista_soma = []
# for i in range(len(lista_b)):
#     lista_soma.append(lista_a[i] + lista_b[i])
# print(lsita_soma)

#----------------------------GERA O MESMO RESULTADO--------------------------------
# lista_soma = []
# for i, _ in enumerate(lista_b):
#     lista_soma.append(lista_a[i] + lista_b[i])
# print(lista_soma)
#------------------------------FORMA PYTHONICA DE FAZER-----------------------------
lista_a = [1,2,3,4,5,6,7]
lista_b = [1,2,3,4]
lista_soma = [x + y for x, y in zip(lista_a, lista_b)]
print(lista_soma)