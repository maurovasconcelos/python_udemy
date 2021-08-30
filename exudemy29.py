import json

d1 = {
    'Pessoa 1': {
        'nome': 'Mauro',
        'idade': 23,
    },
    'Pessoa 2': {
            'nome': 'Marcela',
            'idade': 19,
        },
}
d1_json = json.dumps(d1, indent=True)
with open('abc.json', 'w+') as file:
    file.write(d1_json)
    