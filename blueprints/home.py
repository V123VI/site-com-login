from flask import *

home_bp = Blueprint('home',__name__,template_folder='templates')

@home_bp.route('/home')
def home():
    return render_template('/home/home.html')