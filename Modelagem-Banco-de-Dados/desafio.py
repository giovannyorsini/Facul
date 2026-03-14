import json

# Cadastrando dados dos produtos
produtos = [
    {"nome": "Mouse", "preco": 100, "quantidade": 250},
    {"nome": "Teclado", "preco": 159.90, "quantidade": 87},
    {"nome": "Monitor", "preco": 1249.99, "quantidade": 47}
]

# Salvando dados em formato JSON
with open("produtos.json", "w") as arquivo:
    json.dump(produtos, arquivo)

# Lendo dados do arquivo JSON
with open("produtos.json", "r") as arquivo:
    produtos_carregados = json.load(arquivo)

# Exibindo os dados dos produtos
print("Produtos cadastrados:")
for produto in produtos_carregados:
    print(f"Nome: {produto['nome']}, Preço: R${produto['preco']:.2f}, Quantidade: {produto['quantidade']}")
