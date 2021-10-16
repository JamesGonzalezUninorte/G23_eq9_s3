from flask import Flask, render_template, blueprints, request, redirect, url_for
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
@main.route('/login/', methods=['GET', 'POST'])
def login():
    """fx 
    """
    if request.method == 'POST':
         if request.form.get("iniciosesion"):
            if (request.form['username'] == 'usuario1') & (request.form['password'] == "prueba1"):
                return redirect(url_for('main.profile'))
         elif request.form.get("registrate"):
            if (request.form["form-usuario"] != "") | (request.form["form-password"]!= ""):
                newuser = request.form["form-usuario"]
                newpass = request.form["form-password"]
                return newuser +" "+ newpass
 
    return render_template('pg01.html')

# nota 03
@main.route('/empleado', methods=['GET', 'POST'])

# nota 04
@main.route('/retroalimentacion', methods=['GET', 'POST'])

# nota 05
@main.route('/dashboard_adm', methods=['GET', 'POST'])

# nota 06
@main.route('/eliminar', methods=['GET', 'POST'])

# nota 07
@main.route('/crear', methods=['GET', 'POST'])

# nota 08
@main.route('/editar', methods=['GET', 'POST'])
def editar():
    return render_template("pg08.html")






# fin.

