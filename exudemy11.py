
lista = [
    ['P1', 49],
    ['P2', 93],
    ['P3', 68],
    ['P4', 24],
]

#lambda = função anonima

print(sorted(lista, key=lambda i: i[1], reverse=True))
print(lista)