import sqlite3

conn = sqlite3.connect('finance.db')
cursor = conn.cursor()

# ATUALIZAÇÃO: Adicionando a coluna 'info_parcela'
cursor.execute('''
    CREATE TABLE IF NOT EXISTS gastos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        descricao TEXT NOT NULL,
        categoria TEXT,
        data TEXT NOT NULL,
        valor_original REAL NOT NULL,
        moeda_original TEXT NOT NULL,
        valor_brl REAL NOT NULL,
        info_parcela TEXT 
    )
''')

print("Banco de dados com coluna 'info_parcela' criado com sucesso.")

conn.commit()
conn.close()