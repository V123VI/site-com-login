from flask import *
from db import db, Usuario

registro_bp = Blueprint('REGISTRO', __name__, template_folder='templates/home')

@registro_bp.route('/', methods=['GET', 'POST'])
def registro():
    return render_template('registro.html') 

@registro_bp.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        usuario = request.form.get('usuario')
        senha = request.form.get('senha')

    #acha o nome do usuario no banco de dados
        user = Usuario.query.filter_by(nome=usuario).first()

    #compara nome e senha 
        if user and user.senha == senha:
            # Armazena o ID do usuário na sessão
            #cria a sessão usando o id do usuario que foi procurado no banco de dados
            session['usuario_id'] = user.id
            flash('Login Realizado Com Sucesso')
            return redirect(url_for('home.pagina_home'))  # Redireciona  para home.pagina_home
        
        else:
            return jsonify({'status': 'error', 'message': 'Login Invalido'}), 401
            
    if request.method == 'GET':
        return render_template('registro.html')
