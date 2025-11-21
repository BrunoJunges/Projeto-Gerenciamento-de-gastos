import sqlite3
import os
from werkzeug.security import generate_password_hash

print("--- EXECUTANDO SCRIPT DE INICIALIZAÇÃO DO BANCO DE DADOS ---")

DB_FILE = 'finance.db'
if os.path.exists(DB_FILE):
    os.remove(DB_FILE)
    print(f"--- Banco de dados '{DB_FILE}' antigo removido. ---")

conn = None
try:
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    # 1. Criar a tabela de utilizadores
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL UNIQUE,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    ''')
    print("--- Tabela 'usuarios' criada. ---")

    # 2. Modificar a tabela de gastos para incluir a referência ao utilizador
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
            user_id INTEGER NOT NULL,
            FOREIGN KEY (user_id) REFERENCES usuarios (id)
        )
    ''')
    print("--- Tabela 'gastos' criada com referência a 'user_id'. ---")

    # 3. Inserir o utilizador de teste padrão (login: teste / senha: senha123)
    test_password_hash = generate_password_hash('senha123')
    cursor.execute(
        'INSERT INTO usuarios (email, username, password) VALUES (?, ?, ?)',
        ('teste@exemplo.com', 'teste', test_password_hash)
    )
    print("--- Utilizador de teste ('teste') inserido com sucesso. ---")

    conn.commit()
    print(f"--- SUCESSO: O banco de dados '{DB_FILE}' foi criado e inicializado. ---")

except Exception as e:
    print(f"--- ERRO no script: {e} ---")
    if conn:
        conn.close()
    exit(1)

finally:
    if conn:
        conn.close()