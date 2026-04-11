# comandos somente dentro do MondoDB Shell 
## seleciona e cria um bando
`use escola`
1. Equivalente em Python (usando pymongo):
```python
db = client["nome_do_banco"]
```
- se o banco não existir, será criado automaticamente

## listar bancos existentes
`show dbs`
1. Equivalente em Python:
```python
databases = client.list_database_names()
print(databases)
```

## ver qual banco está em uso
`db`
1. Equivalente em Python:
```python
print(db.name)
```

## deletar banco atual
`db.dropDatabase()`
1. Equivalente em Python:
```python
client.drop_database("nome_do_banco")
```
