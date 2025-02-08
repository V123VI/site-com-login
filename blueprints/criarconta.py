from flask import *
from db import Usuario
criarconta_bp = Blueprint('criar',__name__,template_folder='templates')

@criarconta_bp.route('/cadastro',methods=['GET','POST'])
def cadastro():

    if request.method =='POST':
        usuario = request.form.get('usuario') ###pegar o nome do form do cadastro que ta como: criar.cadastro
        email = request.form.get('email')
        senha = request.form.get('senha')

        print(usuario,senha)
        Usuario.criar_usuario(usuario,email,senha)
        flash('o usuario foi criado','success')


    
    return render_template('criar/criar.html')