import sqlite3

connection = sqlite3.connect('movies.db')

cursor = connection.cursor()

#soLicitando os dados do usuário
id = int(input("Informe o id que deseja remover: \n"))

#Atualizar dados
cursor.execute("""
               DELETE FROM movies WHERE id = ?;""", (id,))

connection.commit()
print("Dados atualizados na tabela")
connection.close()