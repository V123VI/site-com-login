from flask import *
from db import db,Usuario

registro_bp = Blueprint('REGISTRO', __name__, template_folder='templates/home')

@registro_bp.route('/', methods=['GET', 'POST'])
def registro():
    return render_template('registro.html') 

@registro_bp.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        usuario = request.form.get('usuario')
        senha = request.form.get('senha')

        user = Usuario.query.filter_by(nome=usuario).first()

        if user and user.senha == senha:
            flash('Login Realizado Com Sucesso')
            return redirect(url_for('home.home'))
        
        else:
            return jsonify({'status':'error','message':'Login Invalido'}),401
            
    if request.method =='GET':
        return render_template('registro.html')

            