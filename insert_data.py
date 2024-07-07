import sqlite3

# Conectando ao banco de dados
connection = sqlite3.connect("movies.db")
cursor = connection.cursor()

# Deletando a tabela se ela existir
cursor.execute("DROP TABLE IF EXISTS movies")

# Criando a tabela
cursor.execute("""
    CREATE TABLE movies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        year INTEGER NOT NULL,
        score REAL NOT NULL
    )
""")

# Solicitando dados do usuário
name = input("Digite o nome do filme: ")
year = int(input("Digite o ano do filme: "))
score = float(input("Digite a nota do filme: "))

# Inserindo o filme digitado pelo usuário
cursor.execute("""
               INSERT INTO movies(name, year, score)
               VALUES(?, ?, ?)""", (name, year, score))

# Inserindo os outros filmes de forma estática
cursor.execute("""
               INSERT INTO movies(name, year, score)
               VALUES('The Shawshank Redemption', 1994, 9.2)
""")
cursor.execute("""
               INSERT INTO movies(name, year, score)
               VALUES('The Godfather', 1972, 9.2)
""")
cursor.execute("""
               INSERT INTO movies(name, year, score)
               VALUES('The Dark Knight', 2008, 9.0)
""")
cursor.execute("""
               INSERT INTO movies(name, year, score)
               VALUES('12 Angry Men', 1957, 8.9)
""")

# Gravando no banco de dados
connection.commit()
print("Dados inseridos com sucesso")

# Fechando conexão
connection.close()
