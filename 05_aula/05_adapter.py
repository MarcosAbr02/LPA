import sqlite3
import json


class JsonSqliteAdapter:
    def __init__(self, db_name):
        self.db_name = db_name

    def connect(self):
        self.conn = sqlite3.connect(self.db_name)
        self.conn.execute("CREATE TABLE IF NOT EXISTS data "
                          "(id INTEGER PRIMARY KEY, json_data TEXT)")

    def save_data(self, data):
        json_data = json.dumps(data)
        self.conn.execute("INSERT INTO data (json_data) "
                          "VALUES (?)",
                          (json_data,))
        self.conn.commit()

    def load_data(self):
        cursor = self.conn.execute("SELECT json_data FROM data")
        json_data_list = [row[0] for row in cursor.fetchall()]
        data_list = [json.loads(json_data) for json_data in json_data_list]
        return data_list

    def close(self):
        self.conn.close()


# Exemplo de uso
if __name__ == "__main__":
    adapter = JsonSqliteAdapter("data.db")
    adapter.connect()

    data_to_save = [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 30}]
    adapter.save_data(data_to_save)

    loaded_data = adapter.load_data()
    for item in loaded_data:
        print(item)

    adapter.close()
