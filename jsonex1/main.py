"""
JavaScript Object Notation - JSON
JSON (JavaScript Object Notation) é um formato de troca de dados entre sistemas
e programas muito leve e de fácil utilizalção. Muito utilizado por APIs
"""

from dados import *
import json

with open('clientes.json', 'r') as arquivo:
    dados = json.load(arquivo)
print(dados)