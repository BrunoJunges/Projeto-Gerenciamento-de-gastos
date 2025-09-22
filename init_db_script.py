# init_db_script.py
import sqlite3

print("--- EXECUTANDO SCRIPT DE INICIALIZAÇÃO DO BANCO DE DADOS ---")

# O nome do arquivo do banco de dados deve ser o mesmo usado em app.py
DB_FILE = 'finance.db'

conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

# O mesmo comando CREATE TABLE que está no seu database.py
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

conn.commit()
conn.close()

print(f"--- SUCESSO: O banco de dados '{DB_FILE}' foi verificado/criado. ---")
