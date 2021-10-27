from flask import Flask, render_template, blueprints, request, redirect, url_for, flash
from lst_s import lst_Empleados
from werkzeug.security import generate_password_hash, check_password_hash


main = blueprints.Blueprint('main', __name__)

@main.route('/')
def index():
    """fx que maneja la raiz del sitio web.

        Parameters:   Ninguno
        Returns:      Plantilla index.html
    """

    return render_template('pg01.html')

# nota nota xx

# nota 02
@main.route('/login', methods=['GET', 'POST'])
def login():
    """fx 
    """
    if(request.method == 'POST'):
        usuario= request.form['username']
        clave = request.form['userPassword']   
    
    return render_template('pg02_login.html')

# nota 03
@main.route('/empleado', methods=['GET', 'POST'])
def empleado():
    return render_template("pg03.html")


# nota 04
@main.route('/retroalimentacion', methods=['GET', 'POST'])
def retroalimentacion():
    return render_template("pg04.html")


# nota 05
@main.route('/dashboard_adm', methods=['GET', 'POST'])
def dashboard_adm():
    return 'mundo bola' #render_template("pg05.html")


# nota 06
@main.route('/eliminar', methods=['GET', 'POST'])
def eliminar():
    return 'mundo bola' #render_template("pg06.html")


# nota 07
@main.route('/crear', methods=['GET', 'POST'])
def crear():
    return 'mundo bola' #render_template("pg07.html")


# nota 08
@main.route('/editar', methods=['GET', 'POST'])
def editar():
    return 'mundo bola' #render_template("pg08.html")



# fin

