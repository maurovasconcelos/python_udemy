x = 0
while x < 10:
    if x == 3: # se x for igual a 3, x +=1, mais nao printa o 3
        x += 1
        continue # nao vai executar codigos abaixo, nao printa o 3
    print(x)
    x += 1

print('Acabou!')