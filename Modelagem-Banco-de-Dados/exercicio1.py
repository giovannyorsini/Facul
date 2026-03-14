# Criando e salvando um arquivo JSON

import json

# Criando um dicionário com dados de um aluno
aluno = {
    "nome": "Carlos",
    "sobrenome": "Santana",
    "idade": 21,
    "curso": "ADS",
    "ano de inicio": 2025,
    "previsao de conclusao": 2027
}

# Salvando os dados em um arquivo JSON

with open("aluno.json", "w") as arquivo:
    json.dump(aluno, arquivo)

print("Arquivo JSON criado com sucesso!")

# Lendo dados de um arquivo JSON

import json

# Abrindo arquivo JSON

with open("aluno.json", "r") as arquivo:
    dados = json.load(arquivo)
    
# Mostrando os dados carregados

print("Nome:", dados["nome"])
print("Idade:", dados["idade"])
print("Curso:", dados["curso"])
print("Ano de inicio:", dados["ano de inicio"])
print("Previsao de conclusao:", dados["previsao de conclusao"])

# Lista de alunos em JSON

import json

# Lista de alunos
alunos = [
    {"nome": "Ana", "nota": 8.5},
    {"nome": "Pedro", "nota": 7.0},
    {"nome": "Maria", "nota": 9.2},
    {"nome": "João", "nota": 6.8},
    {"nome": "Luisa", "nota": 8.0},
    {"nome": "Carlos", "nota": 7.5}
]

# Salvando no arquivo JSON

with open("alunos.json", "w") as arquivo:
    json.dump(alunos, arquivo)

# Lendo dados de um arquivo JSON

import json

# Abrindo arquivo JSON

with open("alunos.json", "r") as arquivo:
    dados_alunos = json.load(arquivo)

# Mostrando os dados carregados

print("Nome:", dados_alunos[0]["nome"], ", Nota:", dados_alunos[0]["nota"],";")
print("Nome:", dados_alunos[1]["nome"], ", Nota:", dados_alunos[1]["nota"], ";")
print("Nome:", dados_alunos[2]["nome"], ", Nota:", dados_alunos[2]["nota"], ";")
print("Nome:", dados_alunos[3]["nome"], ", Nota:", dados_alunos[3]["nota"], ";")
print("Nome:", dados_alunos[4]["nome"], ", Nota:", dados_alunos[4]["nota"], ";")
print("Nome:", dados_alunos[5]["nome"], ", Nota:", dados_alunos[5]["nota"], ";")
