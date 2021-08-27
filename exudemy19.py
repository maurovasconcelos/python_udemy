# exercicio, somar a compra dos produtos de maneira mais eficiente, osuando apenas uma linha de codigo

carrinho = []

carrinho.append(('produto 1', 30))
carrinho.append(('produto 2', 20))
carrinho.append(('produto 3', 50))
#------------------------------------MANEIRA COMUM-----------------------------------
total = []
# for produto in carrinho:
#     total.append(produto[1])
#print(sum(total))

#---------------------------------MANEIRA TUALIZADA----------------------------------
total = sum([float(y) for x, y in carrinho])            #o total = a soma dos valores(float,pq é dinheiro, Ex: R$12:90)  de cada produto
print(carrinho)
print(total)