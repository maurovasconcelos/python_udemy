'''
Criamos um arquivo.txt w+, zerado , criamos 3 linhas,
'''

file  = open('abc.txt', 'w+')
file.write('Linha 1\n')
file.write('Linha 2\n')
file.write('Linha 3\n')

#--------------------------------------------------------------------------------
'''
colocamos um 'cursor' na posição 0 dele, lemos todas as linhas de uma vez
'''

file.seek(0,0)      #posição relativa do cursor no arquivo, pra poder ser lido corretamente
print('Lendo linhas:')
print(file.read())
print('###########')

#-----------------------------------------------------------------------------
'''
Colocamos o cursor dentro na posição inicial, e lemos linha por linha
'''
file.seek(0,0)
print(file.readline(), end='')      #end='', pra evitar quebra de linha
print(file.readline(), end='')
print(file.readline(), end='')
print('##########')

#--------------------------------------------------------------------------------
'''
Utilizando for pra printar cada linha do arquivo
'''

file.seek(0,0)
for linha in file:
    print(linha, end='')
print('############')

#--------------------------------------------------------------------------------
'''
Maneira mais Pythonica de se fazer
'''
with open('abc.txt', 'r') as file:
    print(file.read())

file.close()

