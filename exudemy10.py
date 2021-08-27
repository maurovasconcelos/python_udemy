''' Criando uma funcao1 que recebe uma funcao2 como aprametro e retorna o valor da funcao2 executada '''

def ola_mundo():
    return 'Ola mundo!'

def mestre(funcao):
    return funcao()

executando = mestre(ola_mundo)
print(executando)

''' Criando uam funcao1 que recebe uma funcao2 como parametro e retorne o valor da funcao2 executada.
Faça a fucnao1 executar duas fuçoes que ceream um numero diferente de argumentos,'''

def mestre(funcao,*args,**kwargs):   #repassando argumentos de uma função para outra
    return funcao(*args,**kwargs)

def diga_oi(nome):
    return f'Oi {nome}'

def saudacao(nome, saudacao):
    return f'{saudacao} {nome}'

executando = mestre(diga_oi, 'Mauro')
executando2= mestre(saudacao,'Mauro', saudacao='Bom dia!')
print(executando)
print(executando2)