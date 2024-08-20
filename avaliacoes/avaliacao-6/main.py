from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3

app = FastAPI()

class Aluno(BaseModel):
    aluno_nome: str
    endereco: str

DATABASE = 'dbalunos.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.post("/criar_aluno/")
def criar_aluno(aluno: Aluno):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("INSERT INTO TB_ALUNO (aluno_nome, endereco) VALUES (?, ?)",
              (aluno.aluno_nome, aluno.endereco))
    conn.commit()
    conn.close()
    return {"status": "Aluno criado"}

@app.get("/listar_alunos/")
def listar_alunos():
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM TB_ALUNO")
    alunos = c.fetchall()
    conn.close()
    return [dict(row) for row in alunos]

@app.get("/listar_um_aluno/{id}")
def listar_um_aluno(id: int):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM TB_ALUNO WHERE id = ?", (id,))
    aluno = c.fetchone()
    conn.close()
    if aluno is None:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    return dict(aluno)

@app.put("/atualizar_aluno/{id}")
def atualizar_aluno(id: int, aluno: Aluno):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("UPDATE TB_ALUNO SET aluno_nome = ?, endereco = ? WHERE id = ?",
              (aluno.aluno_nome, aluno.endereco, id))
    conn.commit()
    conn.close()
    return {"status": "Aluno atualizado"}

@app.delete("/excluir_aluno/{id}")
def excluir_aluno(id: int):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("DELETE FROM TB_ALUNO WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return {"status": "Aluno excluído"}
