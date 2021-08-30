from itertools import count
"""
count - Itertools
"""
"""
Criando indices pra uma lista, utilziando um contador
"""



contador = count(start= 5, step=0.1) # start = Inicia em 5, Step = pulando de x em x,(0.1)em (0.1)
for valor in contador:
    print(round(valor, 2))           #round =arredondando o valor, com 2 casas decimais

    if valor >= 10:
        break

#--------------------------------------------------------------------------------------------------------------------
#maneira mais facil de se criar um indice pra uma lista sem indices

indexador = count()
lista= ['Mauro', 'Marcela', 'Bruno', 'Antonio']

lista = zip(indexador,lista)
print(list(lista))
