import json


class Dog:
    def __init__(self, name, age, weight, height, breed):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
        self.breed = breed

    def __str__(self):
        pass



# Criando um objeto da classe Dog
dog = Dog("Luke", 9, 45, 0.8, "Pastor Alemão")

# Caminho para o arquivo JSON
file_path = "dog.json"

# Convertendo o objeto para um dicionário
dog_dict = {
    "name": dog.name,
    "age": dog.age,
    "weight": dog.weight,
    "height": dog.height,
    "breed": dog.breed
}

# Salvando o dicionário em formato JSON
with open(file_path, "w") as json_file:
    json.dump(dog_dict, json_file, indent=4)

print("Objeto da classe Dog salvo em formato JSON.")
print("Dados salvos em JSON.")


with open(file_path, "r") as json_file:
    loaded_data = json.load(json_file)

print("Dados carrregados do JSON:")
print(loaded_data)

