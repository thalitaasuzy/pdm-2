import sqlite3

def create_db():
    conn = sqlite3.connect('dbalunos.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE TB_ALUNO (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            aluno_nome TEXT,
            endereco TEXT 
        )
    ''')
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_db()
