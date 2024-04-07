import sqlite3

#
# # Conectando ao banco de dados (cria um se não existir)
# conn = sqlite3.connect('animal.db')
#
# # Criando um cursor para executar comandos SQL
# cursor = conn.cursor()
#
# # Criando a tabela
# cursor.execute('''CREATE TABLE IF NOT EXISTS dog(
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 name TEXT,
#                 age INTEGER,
#                 weight REAL,
#                 height REAL,
#                 breed TEXT)''')
#
# # Exemplos de dados para inserir na tabela
# pets_data = [
#     ("Luke", 9, 45, 0.80, "Pastor Alemão"),
#     ("Buddy", 2, 7.2, 0.3, "Golden Retriever"),
#     ("Whiskers", 1, 1.2, 0.15, "Siamese"),
#     ("Max", 4, 5.0, 0.4, "Labrador")
# ]
#
# for pet in pets_data:
#     cursor.execute("INSERT INTO dog"
#                    "(name, age, weight, height, breed)"
#                    "VALUES (?,?,?,?,?)", pet)
#
# # Commit das alterações
# conn.commit()
#
# print("Registros inseridos com sucesso")

# Conectando ao banco de dados
conn = sqlite3.connect("animal.db")

# Criando um cursor para executar comandos SQL
cursor = conn.cursor()

# Selecionando todos os registros da tabela
cursor.execute("SELECT * FROM dog")
rows = cursor.fetchall()

# Mostrando os registros
for row in rows:
    print(f"ID: {row[0]}, "
          f"Name: {row[1]}, "
          f"Age: {row[2]}, "
          f"Weight: {row[3]}, "
          f"Height: {row[4]}, "
          f"Breed: {row[5]}")
