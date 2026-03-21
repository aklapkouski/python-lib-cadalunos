import sqlite3

def conectar():
    return sqlite3.connect("alunos.db")

def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS alunos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            nota1 REAL,
            nota2 REAL
        )

        """
    )

    conn.commit()
    conn.close()


def inserir_registro(nome, n1,n2):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        """
         INSERT INTO alunos (nome, nota1, nota2)
         VALUES(?,?,?)
        """,(nome,n1,n2)
    )

    conn.commit()
    conn.close()

def listar_registros():
    conn = conectar()
    cursor = conn.cursor()
        
    cursor.execute(
        "SELECT * FROM alunos"
    )

    lista = cursor.fetchall()

    conn.close()
    return lista

