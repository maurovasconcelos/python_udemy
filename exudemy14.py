# add (adiciona), update (atualiza), clear, diascart
# union | (une)
# intersection & (todos os elementos presentes nos dois sets)
# diference - (elementos apenas no set da esquerda)
#symetris_diference ^ (elementos que estao nos dois sets, mais nao em ambos)



l1 = ['Luiz', 'Joao', 'Maria']
l2 = ['Luiz', 'Joao', 'Maria', 'Antonio', 'Carlos', 'Maria']

if set(l1) == set(l2):
    print('L1 é igual a L2')
else:
    print('L1 é diferente de L2')