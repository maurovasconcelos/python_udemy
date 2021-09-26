import re


def valida_cpf(cpf):
    cpf = str(cpf)
    cpf = re.sub(r'[^0-9]', '', cpf)

    if not cpf or len(cpf) != 11:
        return False

    novo_cpf = cpf[:-2]             # Elimina os doids últomos digitos do CPF
    reverso = 10                    # Contador reverso
    total = 0

    # Loop do CPF
    for index in range(19):
        if index > 8:               # Primeiro índice vai de 0 a 9,
            index -= 9              # São os 9 primeiros digitos do CPF

        # Valor total da multiplicação
        total += int(novo_cpf[index]) * reverso

        reverso -= 1                # Decrementa o contador reverso
        if reverso < 2:
            reverso = 11
            d = 11 - (total % 11)

            if d > 9:               # Se o digito dor > que 9 o valor é 0
                d = 0
            total = 0               # Zera o total
            novo_cpf += str(d)      # Contatena o digito gerado no novo cpf

    # Evita sequencias. Ex.: 11111111111, 00000000000...
    sequencia = novo_cpf == str(novo_cpf[0]) * len(cpf)

    # Descobri que sequencias avaliam como verdadiero, então também
    # adicione essa checagem aqui
    if cpf == novo_cpf and not sequencia:
        return True
    else:
        return False
