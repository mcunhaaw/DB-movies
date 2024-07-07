import sqlite3

connection = sqlite3.connect('movies.db')

cursor = connection.cursor()

#Lendo os dados da tabela
data = cursor.execute("""
                      SELECT * from movies
""")
print(data.fetchall())

for row in cursor.execute("SELECT * FROM movies ORDER BY year"):
    print(f"{row}")

connection.close()