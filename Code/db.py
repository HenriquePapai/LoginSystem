import sqlite3
import bcrypt

def conectar():
    return sqlite3.connect("database.db")

def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            email TEXT PRIMARY KEY,
            usuario TEXT,
            senha TEXT)
    """)
    conn.commit()
    conn.close()

def criar_usuario(email, usuario, senha):
    try:
        conn = conectar()
        cursor = conn.cursor()
        senha_hash = bcrypt.hashpw(senha.encode(), bcrypt.gensalt())
        cursor.execute("INSERT INTO usuarios (email, usuario, senha) VALUES (?, ?, ?)", (email, usuario, senha_hash))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def verificar_usuario(email, senha):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE email=?", (email,))
    resultado = cursor.fetchone()
    conn.close()

    if resultado:
        senha_hash = resultado[2]
        if bcrypt.checkpw(senha.encode(), senha_hash):
            return resultado[1]
    else:
        return None

# Criar a tabela ao importar
criar_tabela()
