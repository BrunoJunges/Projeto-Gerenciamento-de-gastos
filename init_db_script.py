import sqlite3

print("--- EXECUTANDO SCRIPT DE INICIALIZAÇÃO DO BANCO DE DADOS ---")

DB_FILE = 'finance.db'

try:
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

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

except Exception as e:
    print(f"--- ERRO no script de inicialização do banco de dados: {e} ---")
    # Faz o script falhar para que o deploy pare se houver um erro aqui
    exit(1)
conn.commit()
conn.close()

print(f"--- SUCESSO: O banco de dados '{DB_FILE}' foi verificado/criado. ---")
