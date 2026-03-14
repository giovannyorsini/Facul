import json

# Gerando lista de alunos e notas individuais

alunos = [
    {"nome": "João", "nota": 8.5},
    {"nome": "Maria", "nota": 6.0},
    {"nome": "Pedro", "nota": 9.2},
    {"nome": "Ana", "nota": 5.5}
]

# Salvando dados em formato JSON

with open("alunos.json", "w") as arquivo:
    json.dump(alunos, arquivo)

# Lendo dados do arquivo JSON

with open("alunos.json", "r") as arquivo:
    alunos = json.load(arquivo)

# Exibindo os alunos aprovados (nota >= 7)

for aluno in alunos:
    if aluno["nota"] >= 7:
        print(f"Aluno aprovado: {aluno['nome']}")
