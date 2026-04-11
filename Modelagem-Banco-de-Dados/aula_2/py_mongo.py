from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["escola"]

colecao = db["alunos"]

# inserir
# colecao.insert_one({"nome": "Bruno", "idade": 29})
# colecao.insert_many([
#     { "nome": "Leila", "idade": 27},
#     { "nome": "Rodrigo Alves", "idade": 38 },
#     { "nome": "Simone Rocha", "idade": 34 },
#     { "nome": "Gustavo Henrique", "idade": 29 },
#     { "nome": "Julio Cesar", "idade": 41 }
# ])

# buscar
for aluno in colecao.find():
    print(aluno)

# atualizar
# colecao.update_one(
#     { "nome": "Bruno" },
#     { "$set": { "idade": 30 } }
# )

# colecao.update_many(
#     { "idade": 27},
#     { "$set": { "idade": 20 }},
# )

# remover
colecao.delete_one({ "nome": "Bruno" })
