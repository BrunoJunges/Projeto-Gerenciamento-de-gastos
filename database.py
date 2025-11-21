import sqlite3

conn = sqlite3.connect('finance.db')
cursor = conn.cursor()

# Esquema da tabela de utilizadores
cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT NOT NULL UNIQUE,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )
''')

# Esquema da tabela de gastos com referência ao utilizador
cursor.execute('''
    CREATE TABLE IF NOT EXISTS gastos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        descricao TEXT NOT NULL,
        categoria TEXT,
        data TEXT NOT NULL,
        valor_original REAL NOT NULL,
        moeda_original TEXT NOT NULL,
        valor_brl REAL NOT NULL,
        info_parcela TEXT,
        user_id INTEGER,
        FOREIGN KEY (user_id) REFERENCES usuarios (id)
    )
''')

print("Esquema do banco de dados verificado/criado com sucesso.")

conn.commit()
conn.close()