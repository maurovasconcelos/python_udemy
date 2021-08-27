#exercicio udemy, separar cada repetição em uma lista separada por ponto
#comando usado '.join()'
string = '012345678901234567890123456789012345678901234567890123456789'
n=10

contadores = [i for i in range(0, len(string), n)]
tuplas = [(i, i + n) for i in range(0, len(string), n)]
lista = [string[i: i + n] for i in range(0,len(string), n)] # indice, vai ate indice + n=10, pra cada indice no range de 0 a len da string, pule de n em n,10 em 10
raw = [f'string[{i}:{i + n}]' for i in range(0, len(string), n)]
retorno = '.'.join(lista)

print(contadores)
print(tuplas)
print(raw)
print(lista)
print(retorno)
