import sqlite3
from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime, timedelta
import calendar
from collections import defaultdict
import requests
import os

# Novas importações para gestão de login e segurança de senhas
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user

app = Flask(__name__)
# Chave secreta é essencial para a segurança das sessões de login
app.config['SECRET_KEY'] = 'uma-chave-secreta-muito-segura-e-dificil-de-adivinhar'

API_KEY = 'bc4293db6ecf333a13afd48b'

# --- Configuração do Flask-Login ---
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login' # Se um utilizador não logado tentar aceder a uma página protegida, será redirecionado para a rota 'login'

# --- Modelo de Utilizador para o Flask-Login ---
class User(UserMixin):
    def __init__(self, id, username):
        self.id = id
        self.username = username

@login_manager.user_loader
def load_user(user_id):
    conn = get_db_connection()
    user_data = conn.execute('SELECT id, username FROM usuarios WHERE id = ?', (user_id,)).fetchone()
    conn.close()
    if user_data:
        return User(id=user_data['id'], username=user_data['username'])
    return None

# --- Constantes (Estrutura Original) ---
CATEGORIAS = ["Alimentação", "Locomoção", "Casa", "Lazer", "Despesas inesperadas", "Parcelas/Crédito", "Outros/Indefinível"]
CATEGORIA_ABREVIACOES = {"Alimentação": "Alim", "Locomoção": "Locom", "Casa": "Casa", "Lazer": "Lazer", "Despesas inesperadas": "Desp.In", "Parcelas/Crédito": "Parc.", "Outros/Indefinível": "Outro"}
MOEDAS_SUPORTADAS = ['BRL', 'USD', 'EUR', 'GBP']

# --- Funções de Base (Estrutura Original) ---
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
            return valor_original * dados_taxa['conversion_rate']
    except requests.exceptions.RequestException as e:
        print(f"ERRO: Não foi possível chamar a API de conversão. {e}")
    return valor_original

# --- NOVAS ROTAS DE AUTENTICAÇÃO ---

@app.route('/')
def home_redirect():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = get_db_connection()
        user_data = conn.execute('SELECT * FROM usuarios WHERE username = ?', (username,)).fetchone()
        conn.close()
        if user_data and check_password_hash(user_data['password'], password):
            user = User(id=user_data['id'], username=user_data['username'])
            login_user(user)
            return redirect(url_for('index'))
        else:
            flash('Utilizador ou senha inválidos.', 'danger')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        password2 = request.form['password2']
        if password != password2:
            flash('As senhas não coincidem.', 'danger')
        else:
            conn = get_db_connection()
            user_exists = conn.execute('SELECT id FROM usuarios WHERE username = ? OR email = ?', (username, email)).fetchone()
            if user_exists:
                flash('Utilizador ou email já registado.', 'danger')
                conn.close()
            else:
                hashed_password = generate_password_hash(password)
                conn.execute('INSERT INTO usuarios (email, username, password) VALUES (?, ?, ?)', (email, username, hashed_password))
                conn.commit()
                conn.close()
                flash('Conta criada com sucesso! Faça o login.', 'success')
                return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

# --- ROTAS DA APLICAÇÃO (MODIFICADAS E PROTEGIDAS) ---

# A rota principal '/' agora é a de gastos e exige login
@app.route('/gastos', methods=['GET', 'POST'])
@login_required
def index():
    conn = get_db_connection()
    if request.method == 'POST':
        # Adicionar gasto (lógica original, mas com user_id)
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
        
        # Inserção agora inclui o ID do utilizador logado
        conn.execute('INSERT INTO gastos (descricao, categoria, data, valor_original, moeda_original, valor_brl, info_parcela, user_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
                     (descricao, categoria, data, valor_original, moeda_original, valor_brl, info_parcela, current_user.id))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))

    # Visualizar gastos (lógica original, mas filtrada por user_id)
    filter_year = request.args.get('ano', type=int, default=datetime.now().year)
    filter_month = request.args.get('mes', type=int)

    # Query agora busca apenas os gastos do utilizador logado
    query = 'SELECT * FROM gastos WHERE user_id = ?'
    params = [current_user.id]
    title = "Todos os Gastos"
    if filter_month:
        start_date = f'{filter_year}-{filter_month:02d}-01'
        end_date = f'{filter_year}-{filter_month:02d}-{calendar.monthrange(filter_year, filter_month)[1]}'
        query += ' AND data BETWEEN ? AND ?'
        params.extend([start_date, end_date])
        title = f"Gastos de {calendar.month_name[filter_month].capitalize()}/{filter_year}"

    query += ' ORDER BY data DESC'
    gastos = conn.execute(query, params).fetchall()
    
    # Resto da lógica original
    total_gasto = sum(gasto['valor_brl'] for gasto in gastos)
    gastos_por_categoria = defaultdict(float)
    for gasto in gastos:
        gastos_por_categoria[gasto['categoria']] += gasto['valor_brl']

    grafico_data = []
    if total_gasto > 0:
        for cat_nome in CATEGORIAS:
            valor = gastos_por_categoria[cat_nome]
            percentual = (valor / total_gasto) * 100
            grafico_data.append({
                "categoria_abrev": CATEGORIA_ABREVIACOES.get(cat_nome),
                "percentual": round(percentual, 2),
                "valor_total": round(valor, 2)
            })

    nav_months = []
    today = datetime.now()
    for i in range(4):
        target_date = today - timedelta(days=i * 30)
        if not any(m['ano'] == target_date.year and m['mes'] == target_date.month for m in nav_months):
            nav_months.append({'ano': target_date.year, 'mes': target_date.month, 'nome': calendar.month_name[target_date.month].capitalize()})
            
    min_date_year = today.year
    min_date_month = today.month - 3
    if min_date_month <= 0:
        min_date_month += 12
        min_date_year -= 1
    min_date = f"{min_date_year}-{min_date_month:02d}-01"

    conn.close()

    return render_template('index.html',
                           gastos=gastos, total_gasto=total_gasto, nav_months=nav_months, title=title,
                           current_date=datetime.now().strftime('%Y-%m-%d'), min_date=min_date,
                           categorias=CATEGORIAS, grafico_data=grafico_data, moedas=MOEDAS_SUPORTADAS)

@app.route('/gasto/editar/<int:id>', methods=['POST'])
@login_required
def editar_gasto(id):
    conn = get_db_connection()
    # Verificação de segurança: o gasto pertence ao utilizador?
    gasto = conn.execute('SELECT id FROM gastos WHERE id = ? AND user_id = ?', (id, current_user.id)).fetchone()
    if not gasto:
        conn.close()
        flash('Operação não permitida.', 'danger')
        return redirect(url_for('index'))

    # Lógica original de edição
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

    conn.execute('UPDATE gastos SET descricao = ?, categoria = ?, data = ?, valor_original = ?, moeda_original = ?, valor_brl = ?, info_parcela = ? WHERE id = ?',
                 (descricao, categoria, data, valor_original, moeda_original, valor_brl, info_parcela, id))
    conn.commit()
    conn.close()
    return redirect(request.referrer or url_for('index'))

@app.route('/gasto/excluir/<int:id>', methods=['POST'])
@login_required
def excluir_gasto(id):
    conn = get_db_connection()
    # Verificação de segurança: o gasto pertence ao utilizador?
    gasto = conn.execute('SELECT id FROM gastos WHERE id = ? AND user_id = ?', (id, current_user.id)).fetchone()
    if not gasto:
        conn.close()
        flash('Operação não permitida.', 'danger')
        return redirect(url_for('index'))

    conn.execute('DELETE FROM gastos WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(request.referrer or url_for('index'))

if __name__ == '__main__':
    if not os.path.exists('finance.db'):
        print("ERRO: Banco de dados 'finance.db' não encontrado. Execute o 'init_db_script.py' para criar o banco de dados e o utilizador de teste.")
    else:
        app.run(debug=True)