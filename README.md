# DB-movies
# Inserindo Dados em um Banco de Dados SQLite

Este script Python demonstra como criar um banco de dados SQLite chamado `movies.db`, criar uma tabela chamada `movies`, e inserir dados nela utilizando SQLite e Python.

## Requisitos

- Python 3.x
- SQLite3 (biblioteca padrão do Python)

## Instalação e Uso

1. Clone o repositório ou baixe o script `inserir_data.py`.
2. Execute o script em seu ambiente Python.

## Funcionamento

### Conectando ao Banco de Dados

```python
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
```
# Deletando a Tabela (se existir):
Antes de criar a tabela `movies`, o script verifica se ela já existe no banco de dados `movies.db`.
Se existir, a tabela é removida para garantir que a criação seja limpa e sem conflitos.
```python
cursor.execute("DROP TABLE IF EXISTS movies")
```
# Criando a Tabela:
Utiliza-se a query `CREATE TABLE` para criar uma nova tabela chamada `movies`.
A tabela possui os seguintes campos:
 - `id`: Chave primária que é um número inteiro autoincrementado, garantindo que cada registro tenha um identificador único.
 - `name`: Nome do filme, do tipo texto (`TEXT`), que não pode ser nulo (`NOT NULL`).
 - `year`: Ano de lançamento do filme, um número inteiro que não pode ser nulo.
- `score`: Nota do filme, um número real (`REAL`) que também não pode ser nulo.

```python
cursor.execute("""
    CREATE TABLE movies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        year INTEGER NOT NULL,
        score REAL NOT NULL
    )
""")
```
