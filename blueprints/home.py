from flask import *
from db import Usuario


home_bp = Blueprint('home', __name__, template_folder='templates')

# Decorador para verificar se o usuário está logado
def require_login(func):
    def wrapper(*args, **kwargs):
        if 'usuario_id' not in session:
            return redirect(url_for('REGISTRO.registro'))  # Redireciona para o login se não estiver logado
        return func(*args, **kwargs)
    return wrapper

# Função de rota com o nome correto 'pagina_home'
@home_bp.route('/home', endpoint='pagina_home')  # Explicitamente define o nome do endpoint
@require_login
def pagina_home():
    usuario_id = session.get('usuario_id')
    usuario = Usuario.query.get(usuario_id)
    
    return render_template('/home/home.html',usuario = usuario.nome)
