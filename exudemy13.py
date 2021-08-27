
perguntas = {
    'Pergunta 1' : {
        'pergunta': 'Quanto é 2+2 ?',
        'respostas': {
            'a': '1',
            'b': '6',
            'c': '4',
            'd': '22',},
        'resposta_certa': 'c',
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 2*5 ?',
        'respostas': {
            'a': '10',
            'b': '55',
            'c': '6',
            'd': '62', },
        'resposta_certa': 'a',
    },
    'Pergunta 3': {
        'pergunta': 'Quanto é 4*2 ?',
        'respostas': {
            'a': '44',
            'b': '88',
            'c': '4',
            'd': '8', },
        'resposta_certa': 'd',
    },
}
respostas_certas = 0
for pk, pv in perguntas.items():                 #pra cada key e valor nos items da lista pertungas...
    print(f'{pk}: {pv["pergunta"]}')             #vou printar a key, e o valor "pergunta"

    print('Respostas: ')
    for rk, rv in pv['respostas'].items():       #pra cada key e valor das respostas no valor das perguntas da lista
        print(f'[{rk}]: {rv}')                   #vou printar a key da resposta e o valor dela

    resposta_usuario = input('Sua resposta: ')

    if resposta_usuario == pv['resposta_certa']:
        print('PARABENS !!!, Você acertou ^.^')
        respostas_certas += 1
    else:
        print('Vixe, você errou !')

    print()                                      #print pra pular uma linha entre as perguntas

qtd_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas / qtd_perguntas * 100

print(f'Você acertou {respostas_certas} respostas.')
print(f'Sua porcentagem de acerto foi {porcentagem_acerto:.2f}%')