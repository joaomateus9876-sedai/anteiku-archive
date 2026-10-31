
from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = "anteiku-secret-key"
DATABASE = "anteiku.db"


def conectar_banco():
    conexao = sqlite3.connect(DATABASE)
    conexao.row_factory = sqlite3.Row
    return conexao


def criar_banco():
    conexao = conectar_banco()

    conexao.execute("""
        CREATE TABLE IF NOT EXISTS personagens (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            especie TEXT NOT NULL,
            classificacao TEXT,
            descricao TEXT
        )
    """)

    conexao.commit()
    conexao.close()




@app.route("/")
def home():
    busca = request.args.get("busca", "").strip()

    conexao = conectar_banco()

    if busca:
        personagens = conexao.execute("""
            SELECT * FROM personagens
            WHERE nome LIKE ?
            ORDER BY id DESC
        """, (f"%{busca}%",)).fetchall()
    else:
        personagens = conexao.execute("""
            SELECT * FROM personagens
            ORDER BY id DESC
        """).fetchall()

    total_personagens = conexao.execute(
    "SELECT COUNT(*) FROM personagens"
).fetchone()[0]

    conexao.close()


    return render_template(
        "index.html",
        personagens=personagens,
        total_personagens=total_personagens
    )



@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    nome = request.form.get("nome", "").strip()
    especie = request.form.get("especie", "").strip()
    classificacao = request.form.get("classificacao", "").strip()
    descricao = request.form.get("descricao", "").strip()

    if not nome or not especie:
        return "Nome e espécie são obrigatórios.", 400

    conexao = conectar_banco()

    conexao.execute("""
        INSERT INTO personagens (nome, especie, classificacao, descricao)
        VALUES (?, ?, ?, ?)
    """, (nome, especie, classificacao, descricao))

    conexao.commit()
    conexao.close()

    flash("Personagem registrado no arquivo com sucesso!", "success")
    return redirect(url_for("home"))

@app.route("/editar/<int:id>")
def editar(id):
    conexao = conectar_banco()

    personagem = conexao.execute(
        "SELECT * FROM personagens WHERE id = ?",
        (id,)
    ).fetchone()

    conexao.close()

    if personagem is None:
        return "Personagem não encontrado.", 404

    return render_template(
        "editar.html",
        personagem=personagem
    )


@app.route("/salvar_edicao/<int:id>", methods=["POST"])
def salvar_edicao(id):
    nome = request.form.get("nome", "").strip()
    especie = request.form.get("especie", "").strip()
    classificacao = request.form.get("classificacao", "").strip()
    descricao = request.form.get("descricao", "").strip()

    if not nome or not especie:
        return "Nome e espécie são obrigatórios.", 400

    conexao = conectar_banco()

    personagem = conexao.execute(
        "SELECT id FROM personagens WHERE id = ?",
        (id,)
    ).fetchone()

    if personagem is None:
        conexao.close()
        return "Personagem não encontrado.", 404

    conexao.execute("""
        UPDATE personagens
        SET nome = ?, especie = ?, classificacao = ?, descricao = ?
        WHERE id = ?
    """, (nome, especie, classificacao, descricao, id))

    conexao.commit()
    conexao.close()

    flash("Registro atualizado com sucesso!", "success")
    return redirect(url_for("home"))


@app.route("/excluir/<int:id>", methods=["POST"])
def excluir(id):
    conexao = conectar_banco()

    personagem = conexao.execute(
        "SELECT id FROM personagens WHERE id = ?",
        (id,)
    ).fetchone()

    if personagem is None:
        conexao.close()
        return "Personagem não encontrado.", 404

    conexao.execute(
        "DELETE FROM personagens WHERE id = ?",
        (id,)
    )

    conexao.commit()
    conexao.close()

    flash("Registro removido do arquivo.", "success")
    return redirect(url_for("home"))


if __name__ == "__main__":
    criar_banco()
    print("Banco de dados preparado com sucesso!")
    app.run(debug=True)
