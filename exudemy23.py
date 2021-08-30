"""
Combinations, Permutations e Products = Itertools
Combinação - Ordem não importa
Permutação - Ordem improta
Ambos não repetem valores unicos
Produto - Ordem importa e repete valores unicos
"""
from itertools import  combinations, permutations, product

pessoas = ['Luiz', 'André', 'Eduardo', 'Leticia', 'Fabrício', 'Rose']

for grupo in product(pessoas, repeat=2):
    print(grupo)