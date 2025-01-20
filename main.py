from flask import *
from blueprints.registro import registro_bp
from blueprints.home import home_bp
from db import *
import click

app = Flask(__name__)
app.secret_key = '12012109'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



db.init_app(app)

app.register_blueprint(registro_bp)  # Registra o Blueprint de Registro
app.register_blueprint(home_bp)  # Registra o Blueprint de Home

##rodar as operações: 
@app.cli.command('rodar')
def rodar():
    with app.app_context():
        Usuario.criar_usuario('vini','teste@gmail.com','123')
        


if __name__ == "__main__":
    app.run(debug=True)

