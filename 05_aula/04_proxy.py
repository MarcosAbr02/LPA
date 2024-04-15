import sqlite3


class Dog:
    def __init__(self, name, age, weight, height, breed):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
        self.breed = breed


# Proxy para interagir com o banco de dados SQLite3
class DbProxy:
    def __init__(self, database_path="dogs.db"):
        self.database_path = database_path

    def insert_dog(self, new_dog):
        conn = sqlite3.connect(self.database_path)
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS dogs(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        weight REAL,
        height REAL,
        breed TEXT
        )""")

        cursor.execute("INSERT INTO dogs"
                       "(name, age, weight, height, breed)"
                       "VALUES(?,?,?,?,?)",
                       (new_dog.name,
                        new_dog.age,
                        new_dog.weight,
                        new_dog.height,
                        new_dog.breed))

        conn.commit()
        conn.close()
        print("Dog inserted successfully")

    def get_all_dogs(self):
        conn = sqlite3.connect(self.database_path)
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM dogs")
        rows = cursor.fetchall()

        dogs = []
        for row in rows:
            dogs.append(Dog(row[1], row[2], row[3], row[4], row[5]))

        conn.close()
        return dogs


# Criando um objeto Dog
dog = Dog("Luke", 10, 45, 0.8, "Pastor Alemão")

# Usando o Proxy para inserir o objeto no banco de dados
proxy = DbProxy()
proxy.insert_dog(dog)

# Usando o Proxy para buscar todos os cachorros no banco de dados
all_dogs = proxy.get_all_dogs()

for d in all_dogs:
    print(f"Name: {d.name}, "
          f"Age: {d.age}, "
          f"Weight: {d.weight}, "
          f"Height: {d.height},"
          f"Breed: {d.breed}")
