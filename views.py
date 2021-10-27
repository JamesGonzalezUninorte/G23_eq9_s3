from flask import Flask, render_template, blueprints, request, redirect, url_for, flash
from formulario import pgLogin
from markupsafe import escape
import os
#from werkzeug.security import generate_password_hash, check_password_hash


main=Flask(__name__)
main.secret_key=os.urandom(24)

@main.route('/')
@main.route('/index/')
@main.route('/home/')
def index():
    return render_template('pg01_inicio.html')

@main.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method=='GET':
        frm=pgLogin()
        return render_template('pg02_login.html', form=frm, titulo='Acceso de usuarios')
    else:
        #recuperar los datos del formulario
        usr=escape(request.form["user"]) #dificulta la inyeccion de codigo
        cla=escape(request.form["passw"]) #dificulta la inyeccion de codigo
        #validar los datos del lado del servidor
        sal=''
        if len(usr.strip())<10:
            sal+='El usuario es requerido y su longitud debe ser min 10 caracteres'
        if len(cla.strip())<8:
            sal+='La contraseña es requerido y su longitud debe ser min 8 caracteres'
        if sal=='':
            sal='Los datos son validos, deberiamos consultar a los 80'
        sal+='<a href="/">Volver al inicio</a>'
    return sal   

# nota 03
@main.route('/empleado/', methods=['GET', 'POST'])
def empleado():
    return render_template("pg03_empleado.html")


# nota 04
@main.route('/retroalimentacion/', methods=['GET', 'POST'])
def retroalimentacion():
    return render_template("pg04_desempeño.html")

'''
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
    '''
# fin

if __name__ == '__main__':
    main.run(debug=True)