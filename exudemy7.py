# def saudacao(saudacao, nome):
#     print(f'{saudacao} {nome}')
#
# saudacao('ola', 'pessoa')
# saudacao('hey', 'fulano')

# def soma(n1,n2,n3):
#     print(n1+n2+n3)
#
# soma(2,1,3)
# soma(1,1,1)
# soma(2,1,1)

def aumento_percentual(valor,percentual):
    return valor+(valor*percentual/100)

ap = aumento_percentual(50,10)
print(ap)
ap = aumento_percentual(100,10)
print(ap)
ap = aumento_percentual(15,100)
print(ap)


