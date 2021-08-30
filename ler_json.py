import json

with open('abc.json', 'r') as file:
    d1_json = file.read()           #lendo o arquivo.json
    d1_json = json.loads(d1_json)   #convertendo de volta o .json para um dicionario

for k, v in d1_json.items():        #printando cada um dos valores convertidos de json de volta  a dicionario
    print(k)
    for k1, v1 in v.items():
        print(k1, v1)
    