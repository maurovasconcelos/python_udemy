
def saudacao(msg='ola', nome='usiario'):
    nome = nome.replace('e', '3')
    msg = msg.replace('e','3')
    return f'{msg} {nome}'

variavel = saudacao()

print(variavel)