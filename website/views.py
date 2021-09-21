from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/trajetoriapessoal')
def trajetoriapessoal():
    return render_template("trajetoriapessoal.html")

@views.route('/contato')
def contato():
    return render_template("contato.html")

@views.route('/trajetoriaprofissional')
def trajprofissional():
    return render_template("trajetoriaprofissional.html")


