# Criando e salvando um arquivo JSON

import json

# Criando um dicionário com dados de um aluno
aluno = {
    "nome": "Carlos",
    "idade": 21,
    "curso": "ADS"
}

# Salvando os dados em um arquivo JSON

with open("aluno.json", "w") as arquivo:
    json.dump(aluno, arquivo)

print("Arquivo JSON criado com sucesso!")

# 