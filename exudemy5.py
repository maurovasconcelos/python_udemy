texto = 'Python'
nova_string = ''

#continue - pula para o proximo laço
#break - para de executar o laço

for letra in texto:
    if letra == 't':

        nova_string += letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
        break
    else:
        nova_string += letra

print(nova_string)