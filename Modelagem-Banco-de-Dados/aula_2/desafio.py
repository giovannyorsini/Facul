from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
# criando o bando "loja" e a colecao "produtos"
db = client["loja"]
colecao = db["produtos"]

# adicionando produtos ao estoque
# colecao.insert_many([
#     { "nome": "Notebook", "preco": 3500, "estoque": 10 },
#     { "nome": "Mouse", "preco": 80, "estoque": 50 },
#     { "nome": "Teclado", "preco": 150, "estoque": 30 },
#     { "nome": "Processador", "preco": 2500, "estoque": 5 },
#     { "nome": "Monitor", "preco": 900, "estoque": 20 },
#     { "nome": "Impressora", "preco": 600, "estoque": 15 },
#     { "nome": "Webcam", "preco": 120, "estoque": 25 },
#     { "nome": "Headset", "preco": 200, "estoque": 40 },
#     { "nome": "Caixa de Som", "preco": 180, "estoque": 35 },
#     { "nome": "HD Externo", "preco": 400, "estoque": 18 },
#     { "nome": "Pen Drive", "preco": 60, "estoque": 60 },
#     { "nome": "Cadeira Gamer", "preco": 1200, "estoque": 8 },
#     { "nome": "Mesa para Computador", "preco": 700, "estoque": 12 },
#     { "nome": "Roteador Wi-Fi", "preco": 250, "estoque": 22 },
#     { "nome": "Placa de Vídeo", "preco": 2500, "estoque": 5 },
#     { "nome": "Memória RAM", "preco": 300, "estoque": 28 }
# ])

# consultando valores acima de 300
produtos_caros = colecao.find({ "preco": {"$gt": 300} })

for produto in produtos_caros:
    print(produto)
print("\n")

# atualizar estoque
print(colecao.find_one({ "nome": "Mouse" })) # print para consulta pré-atualização
print("\n")

colecao.update_one(
    { "nome": "Mouse" }, 
    { "$set": {"estoque": 45} }
)

print(colecao.find_one({ "nome": "Mouse" }))
print("\n")

#remover produto
colecao.delete_one({ "nome": "Teclado" })

# lista de todos os produtos restantes
produtos = colecao.find()
for produto in produtos:
    print(produto)
