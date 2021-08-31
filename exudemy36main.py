from exudemy36 import Cliente

cliente1 = Cliente('Mauro', 23)
cliente1.insere_endereco('Belo Horizonte', 'MG')
print(cliente1.nome)
cliente1.lista_enderecos()
print()

cliente2 = Cliente('Marcela', 19)
cliente2.insere_endereco('São Paulo', 'SP')
cliente2.insere_endereco('Venda Nova', 'MG')
print(cliente2.nome)
cliente2.lista_enderecos()
print()

cliente3 = Cliente('Antonio', 54)
cliente3.insere_endereco('Paraná', 'PR')
print(cliente3.nome)
cliente3.lista_enderecos()
print()