def func(*args, **kwargs):                  # *args = serve pra receber varios argumentos
    print(args)                             # **kwargs = keyword arguments, basicamente vc define a key dos argumentos

    idade = kwargs['idade']
    print(idade)

lista = [1,2,3,4,5]
lista2 = [10,20,30,40,50]
func(*lista, *lista2, nome='Mauro', sobrenome='Vasconcelos', idade=23)  # *'variavel', desempacota o que tiver dentro em uma lista