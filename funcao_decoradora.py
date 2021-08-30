
def master(funcao):                     #função decoradora
    def slave(*args, **kwargs):
        print('Agora estou decorada.')
        funcao(*args, **kwargs)
    return slave

@master                                 #decorador
def fala_oi():
    print('Oi')

@master
def outra_funcao(msg):
    print(msg)

#fala_oi = master(fala_oi)

outra_funcao('Ola Estudo de Python, chama no reles')