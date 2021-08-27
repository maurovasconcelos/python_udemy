
t1 = (1,2,3,4,5,6)
t1 = list(t1)           #transofrmando tupla em lista
t1[1] = 3000            #mudando valor da tupla/lista
t1 = tuple(t1)          #transformando a lista em tupla novamente

print(t1)


clientes = {                            # uma lista com varias listas dentro
    'cliente1': {
        'nome' : 'Mauro',
        'sobrenome' : 'Vasconcelos',
    },
    'clientes2': {
        'nome' : 'Marcela',
        'sobrenome' : 'Rezende',
    },
}

for clientes_k, clientes_v in clientes.items():  # pra cada chave  e cara valor dentro da lista clientes.items
    print(f'Exibindo {clientes_k}')              # printar a key
    for dados_k, dados_v in clientes_v.items():  # pra cada key e valor na lista de items de clientes
        print(f'\t{dados_k} = {dados_v}')        # printar a key e o valor de cada um


d1 = {
    1: 2,
    2: 3,
    4: 5
}

d2 = {
    'a' : 'b',
    'c' : 'd',
}

d1.update(d2)       #update, basicamente inclui o que foi passado para para outra variavel/lista
print(d1)