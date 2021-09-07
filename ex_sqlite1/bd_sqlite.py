import sqlite3

conexao = sqlite3.connect('basededados.db')
cursor = conexao.cursor()  # cria um 'mouse' la dentro
# cursor.execute('CREATE TABLE IF NOT EXISTS clientes ('  # Cria uma tabela se ela nao existir, com o nome 'clientes'
#                'id INTEGER PRIMARY KEY AUTOINCREMENT,'  # ela é um id Inteiro, e uma Key que se autocria
#                'nome TEXT,'  # possue nome = TEXT
#                'peso REAL'  # e peso = que é um numero real
#                ')')

# cursor.execute(
#     'INSERT INTO clientes (nome, peso) VALUES (?, ?)',
#     ('Marcela', 19))  # insira na lista nas posiçoes tal, os valores tal
# cursor.execute(
#     'INSERT INTO clientes (nome, peso) VALUES (:nome, :peso)',
#     {'nome': 'Joaozinho', 'peso': 25}
# )
# cursor.execute(
#     'INSERT INTO clientes VALUES (:id, :nome, :peso)',
#     {'id': None, 'nome': 'Daniel', 'peso': 113}
# )
# conexao.commit()

# cursor.execute(
#     'UPDATE clientes SET nome=:nome WHERE id=:id',
#     {'nome': 'Bruna', 'id': 5}
# )
cursor.execute('DELETE FROM clientes WHERE id=:id',
               {'id': 2})
conexao.commit()

cursor.execute('SELECT * FROM clientes')  # o base de dados, seleciona tudo de clientes


for linha in cursor.fetchall():  # comandao que busca e executa os comandos
    identificador, nome, peso = linha
    print(identificador, nome, peso)

cursor.close()
conexao.close()
