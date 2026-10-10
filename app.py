from flask import Flask, request, redirect, render_template_string
import sqlite3
from datetime import date

app = Flask(__name__)
DB = "finansys.db"

def conectar():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    return conn

def preparar_banco():
    with conectar() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS transacoes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                descricao TEXT NOT NULL,
                valor REAL NOT NULL,
                categoria TEXT NOT NULL,
                tipo TEXT NOT NULL,
                data TEXT NOT NULL
            )
        """)

PAGINA = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>FinanSys</title>
<style>
body{font-family:Arial,sans-serif;background:#f1f5f9;color:#172033;
margin:0;padding:20px}
main{max-width:850px;margin:auto}
h1{color:#176b50}
.card{background:white;padding:18px;border-radius:12px;
margin:14px 0;box-shadow:0 2px 8px #0001}
.resumo{display:flex;gap:12px;flex-wrap:wrap}
.resumo .card{flex:1;min-width:140px}
input,select,button{box-sizing:border-box;padding:11px;margin:5px 0;
width:100%;border:1px solid #ccd3dd;border-radius:7px}
button{background:#176b50;color:white;font-weight:bold;cursor:pointer}
table{width:100%;border-collapse:collapse}
th,td{text-align:left;padding:9px;border-bottom:1px solid #ddd}
.excluir{background:#b42318}
.valor{font-weight:bold}
</style>
</head>
<body><main>
<h1>FinanSys</h1>
<p>Controle financeiro pessoal</p>
<div class="resumo">
<div class="card"><b>Saldo total</b><h2>R$ {{ "%.2f"|format(saldo) }}</h2></div>
<div class="card"><b>Receitas</b><h2>R$ {{ "%.2f"|format(receitas) }}</h2></div>
<div class="card"><b>Despesas</b><h2>R$ {{ "%.2f"|format(despesas) }}</h2></div>
</div>
<div class="card">
<h2>Nova transação</h2>
<form method="post" action="/adicionar">
<label>Descrição</label><input name="descricao" required maxlength="100">
<label>Valor (R$)</label><input name="valor" type="number" min="0.01" step="0.01" required>
<label>Categoria</label>
<select name="categoria" required>
<option>Alimentação</option><option>Transporte</option>
<option>Moradia</option><option>Salário</option>
<option>Lazer</option><option>Saúde</option><option>Outros</option>
</select>
<label>Tipo</label><select name="tipo">
<option value="receita">Receita</option>
<option value="despesa">Despesa</option></select>
<label>Data</label><input name="data" type="date" value="{{ hoje }}" required>
<button type="submit">Adicionar transação</button>
</form></div>
<div class="card"><h2>Histórico</h2>
{% if transacoes %}
<div style="overflow-x:auto"><table>
<tr><th>Descrição</th><th>Valor</th><th>Tipo</th><th>Data</th><th></th></tr>
{% for t in transacoes %}
<tr><td>{{ t['descricao'] }}</td>
<td>R$ {{ "%.2f"|format(t['valor']) }}</td>
<td>{{ t['tipo'] }}</td><td>{{ t['data'] }}</td>
<td><form method="post" action="/excluir/{{ t['id'] }}">
<button class="excluir" type="submit">Excluir</button></form></td></tr>
{% endfor %}</table></div>
{% else %}<p>Nenhuma transação cadastrada.</p>{% endif %}
</div></main></body></html>
"""

@app.route("/")
def inicio():
    with conectar() as conn:
        transacoes = conn.execute(
            "SELECT * FROM transacoes ORDER BY data DESC, id DESC"
        ).fetchall()
        receitas = sum(t["valor"] for t in transacoes if t["tipo"] == "receita")
        despesas = sum(t["valor"] for t in transacoes if t["tipo"] == "despesa")
    return render_template_string(
        PAGINA, transacoes=transacoes, receitas=receitas,
        despesas=despesas, saldo=receitas-despesas, hoje=date.today().isoformat()
    )

@app.route("/adicionar", methods=["POST"])
def adicionar():
    descricao = request.form.get("descricao", "").strip()
    categoria = request.form.get("categoria", "Outros")
    tipo = request.form.get("tipo", "")
    data_transacao = request.form.get("data", "")
    try:
        valor = float(request.form.get("valor", "0").replace(",", "."))
        if not descricao or valor <= 0 or tipo not in ("receita", "despesa"):
            return "Dados inválidos. Volte e confira os campos.", 400
        date.fromisoformat(data_transacao)
    except (ValueError, TypeError):
        return "Valor ou data inválidos. Volte e confira os campos.", 400
    with conectar() as conn:
        conn.execute(
            "INSERT INTO transacoes (descricao, valor, categoria, tipo, data) VALUES (?, ?, ?, ?, ?)",
            (descricao, valor, categoria, tipo, data_transacao)
        )
    return redirect("/")

@app.route("/excluir/<int:id>", methods=["POST"])
def excluir(id):
    with conectar() as conn:
        conn.execute("DELETE FROM transacoes WHERE id = ?", (id,))
    return redirect("/")

if __name__ == "__main__":
    preparar_banco()
    app.run(debug=True)
