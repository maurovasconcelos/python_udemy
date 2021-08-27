from itertools import zip_longest, count
"""
Zip - Unindo iteraveis
Zip-longest - Intertools
"""
indice = count()
cidades = ['Sao Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo']
estados = ['SP', 'MG', 'BA',]


cidades_estados = zip(          #POSSO zipar/ unir as duas lsitas, e transoformar em listas
    indice,
    cidades,
    estados
)

for indice, estados, cidades in cidades_estados:
    print(indice, estados, cidades)
