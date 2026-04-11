# atualizando dados de um produto no arquivo JSON
import json

with open('produtos.json', 'r') as arq:
    produto = json.load(arq)

# Atualizando a quantidade do produto
produto["quantidade"] = 50

# Salvando as alterações de volta no arquivo JSON
with open('produtos.json', 'w') as arq:
    json.dump(produto, arq)
    
print("Quantidade atualizada com sucesso!")