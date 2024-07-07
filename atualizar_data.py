import sqlite3

connection = sqlite3.connect('movies.db')

cursor = connection.cursor()

#soLicitando os dados do usuário
id = int(input("Informe o id que deseja atualizar: \n"))
name = input("Informe um novo nome: \n")

#Atualizar dados
cursor.execute("""
               UPDATE movies set name = ? WHERE id = ?
""", (name, id))
connection.commit()
print("Dados atualizados na tabela")
connection.close()