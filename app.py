import sqlite3
from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime, timedelta
import calendar
from collections import defaultdict
import requests

app = Flask(__name__)

API_KEY = 'bc4293db6ecf333a13afd48b' 

CATEGORIAS = [
    "Alimentação", "Locomoção", "Casa", "Lazer", 
    "Despesas inesperadas", "Parcelas/Crédito", "Outros/Indefinível"
]

CATEGORIA_ABREVIACOES = {
    "Alimentação": "Alim",
    "Locomoção": "Locom",
    "Casa": "Casa",
    "Lazer": "Lazer",
    "Despesas inesperadas": "Desp.In",
    "Parcelas/Crédito": "Parc.",
    "Outros/Indefinível": "Outro"
}

MOEDAS_SUPORTADAS = ['BRL', 'USD', 'EUR', 'GBP']

def get_db_connection():
    conn = sqlite3.connect('finance.db')
    conn.row_factory = sqlite3.Row
    return conn

def obter_valor_convertido(valor_original, moeda_original):
    if moeda_original == 'BRL':
        return valor_original
    try:
        url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{moeda_original}/BRL"
        response = requests.get(url)
        response.raise_for_status()
        dados_taxa = response.json()
        if dados_taxa.get('result') == 'success':
            taxa_conversao = dados_taxa['conversion_rate']
            return valor_original * taxa_conversao
    except requests.exceptions.RequestException as e:
        print(f"ERRO: Não foi possível chamar a API de conversão. {e}")
        return valor_original
    return valor_original

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        descricao = request.form['descricao']
        valor_original = float(request.form['valor'])
        moeda_original = request.form['moeda']
        categoria = request.form['categoria']
        data = request.form['data']
        valor_brl = obter_valor_convertido(valor_original, moeda_original)

        info_parcela = None
        if categoria == 'Parcelas/Crédito':
            parcela_atual = int(request.form.get('parcela_atual', 1))
            parcela_total = int(request.form.get('parcela_total', 1))
            info_parcela = f"{parcela_atual:02d}/{parcela_total:02d}"

        conn = get_db_connection()
        conn.execute('INSERT INTO gastos (descricao, categoria, data, valor_original, moeda_original, valor_brl, info_parcela) VALUES (?, ?, ?, ?, ?, ?, ?)',
                     (descricao, categoria, data, valor_original, moeda_original, valor_brl, info_parcela))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))

    conn = get_db_connection()
    filter_year = request.args.get('ano', type=int, default=datetime.now().year)
    filter_month = request.args.get('mes', type=int)

    query = 'SELECT * FROM gastos'
    params = []
    title = "Todos os Gastos"
    if filter_month:
        start_date = f'{filter_year}-{filter_month:02d}-01'
        end_date = f'{filter_year}-{filter_month:02d}-{calendar.monthrange(filter_year, filter_month)[1]}'
        query += ' WHERE data BETWEEN ? AND ?'
        params.extend([start_date, end_date])
        title = f"Gastos de {calendar.month_name[filter_month].capitalize()}/{filter_year}"

    query += ' ORDER BY data DESC'
    gastos = conn.execute(query, params).fetchall()
    
    total_gasto = sum(gasto['valor_brl'] for gasto in gastos)
    gastos_por_categoria = defaultdict(float)
    for gasto in gastos:
        gastos_por_categoria[gasto['categoria']] += gasto['valor_brl']

    grafico_data = []
    for categoria_nome_completo in CATEGORIAS:
        valor_da_categoria = gastos_por_categoria[categoria_nome_completo]
        percentual = (valor_da_categoria / total_gasto) * 100 if total_gasto > 0 else 0
        grafico_data.append({
            "categoria_abrev": CATEGORIA_ABREVIACOES.get(categoria_nome_completo),
            "percentual": round(percentual, 2),
            "valor_total": round(valor_da_categoria, 2)
        })

    nav_months = []
    today = datetime.now()
    for i in range(4):
        target_date = today - timedelta(days=i*30)
        year, month = target_date.year, target_date.month
        month_name = calendar.month_name[month].capitalize()
        if (year, month) not in [(m['ano'], m['mes']) for m in nav_months]:
            nav_months.append({'ano': year, 'mes': month, 'nome': month_name})
            
    min_date_year = today.year
    min_date_month = today.month - 3
    if min_date_month <= 0:
        min_date_month += 12
        min_date_year -= 1
    min_date = f"{min_date_year}-{min_date_month:02d}-01"

    conn.close()

    return render_template('index.html',
                           gastos=gastos,
                           total_gasto=total_gasto,
                           nav_months=nav_months,
                           title=title,
                           current_date=datetime.now().strftime('%Y-%m-%d'),
                           min_date=min_date,
                           categorias=CATEGORIAS,
                           grafico_data=grafico_data,
                           moedas=MOEDAS_SUPORTADAS)

@app.route('/gasto/editar/<int:id>', methods=['POST'])
def editar_gasto(id):
    descricao = request.form['descricao']
    valor_original = float(request.form['valor_original'])
    moeda_original = request.form['moeda_original']
    categoria = request.form['categoria']
    data = request.form['data']
    valor_brl = obter_valor_convertido(valor_original, moeda_original)

    info_parcela = None
    if categoria == 'Parcelas/Crédito':
        parcela_atual = int(request.form.get('parcela_atual_edit', 1))
        parcela_total = int(request.form.get('parcela_total_edit', 1))
        info_parcela = f"{parcela_atual:02d}/{parcela_total:02d}"

    conn = get_db_connection()
    conn.execute('UPDATE gastos SET descricao = ?, categoria = ?, data = ?, valor_original = ?, moeda_original = ?, valor_brl = ?, info_parcela = ? WHERE id = ?',
                 (descricao, categoria, data, valor_original, moeda_original, valor_brl, info_parcela, id))
    conn.commit()
    conn.close()
    return redirect(request.referrer or url_for('index'))

@app.route('/gasto/excluir/<int:id>', methods=['POST'])
def excluir_gasto(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM gastos WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(request.referrer or url_for('index'))

if __name__ == '__main__':
    if API_KEY == 'SUA_API_KEY_AQUI':
        print("\n\n*** ATENÇÃO: A API Key não foi configurada no arquivo app.py! A conversão de moeda não funcionará. ***\n\n")
    app.run(debug=True)