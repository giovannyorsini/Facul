import json

# Criando um estoque de produtos
estoque = [
    {"nome": "Teclado", "preco": 120, "quantidade": 10},
    {"nome": "Monitor", "preco": 900, "quantidade": 5},
    {"nome": "Mouse", "preco": 100, "quantidade": 50},
    {"nome": "Impressora", "preco": 500, "quantidade": 2},
    {"nome": "Cadeira", "preco": 300, "quantidade": 15},
    {"nome": "Mesa", "preco": 700, "quantidade": 7},
    {"nome": "Notebook", "preco": 2500, "quantidade": 3},
    {"nome": "Headset", "preco": 150, "quantidade": 20},
    {"nome": "Webcam", "preco": 200, "quantidade": 8},
    {"nome": "Roteador", "preco": 250, "quantidade": 12}
]

# Salvando o estoque em um arquivo JSON
with open("estoque.json", "w") as arquivo:
    json.dump(estoque, arquivo)

print("Estoque salvo!")

# Checando o estoque de cada produto e listando os produtos com quantidade menor que 5

with open("estoque.json", "r") as arquivo:
    estoque_carregado = json.load(arquivo)

print("Produtos com quantidade menor que 5:")
for produto in estoque_carregado:
    if produto["quantidade"] < 5:
        print(f" - {produto['nome']}: {produto['quantidade']} unidades\n[ATENÇÃO: Reabastecer o estoque desse produto!]")
