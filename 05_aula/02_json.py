import json

# Dados a serem salvos em um arquivo JSON
data = {
    "name": "Luke",
    "age": 9,
    "weight": 45,
    "height": 0.8,
    "breed": "pastor alemão"
}

# Caminho para o arquivo JSON
file_path = "data.json"

# Salvar dados em formato JSON no arquivo
with open(file_path, "w") as json_file:
    json.dump(data, json_file, indent=4)

print("Dados salvos em JSON.")

# Carregar dados de um arquivo JSON
with open(file_path, "r") as json_file:
    loaded_data = json.load(json_file)

print("Dados carrregados do JSON:")
print(loaded_data)
