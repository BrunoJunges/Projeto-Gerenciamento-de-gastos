import sqlite3
import os

print("--- EXECUTANDO SCRIPT DE INICIALIZAÇÃO DO BANCO DE DADOS ---")

DB_FILE = 'finance.db'
conn = None  # Inicializa a variável de conexão

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

    # CORREÇÃO: O commit deve acontecer ANTES de fechar a conexão
    conn.commit()
    print(f"--- SUCESSO: O banco de dados '{DB_FILE}' foi verificado/criado. ---")

except Exception as e:
    print(f"--- ERRO no script de inicialização do banco de dados: {e} ---")
    # Faz o script falhar para que o deploy pare se houver um erro aqui
    if conn:
        conn.close() # Tenta fechar a conexão se ela foi aberta
    exit(1)

finally:
    # Garante que a conexão seja sempre fechada, mesmo se houver um erro
    if conn:
        conn.close()
