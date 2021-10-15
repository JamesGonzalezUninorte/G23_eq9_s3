from flask import Flask, render_template, blueprints, request, redirect, url_for

main = blueprints.Blueprint('main', __name__)
@main.route('/')
def index():
    """Función que maneja la raiz del sitio web.

        Parameters:
        Ninguno

        Returns:
        Plantilla index.html
    """
    
    return render_template('pg01.html')

# nota nota xx

# nota 02
@main.route('/login/', methods=('GET', 'POST'))

# nota 03
@main.route('/empleado', methods=('GET', 'POST'))

# nota 04
@main.route('/retroalimentacion', methods=('GET', 'POST'))

# nota 05
@main.route('/dashboard_adm', methods=('GET', 'POST'))

# nota 06
@main.route('/eliminar', methods=('GET', 'POST'))

# nota 07
@main.route('/crear', methods=('GET', 'POST'))

# nota 08
@main.route('/editar', methods=('GET', 'POST'))
def editar():
    return render_template("pg08.html")



lst_Empleados=[
    {'nombre':'Empleado Uno',  'id':'12345', 'cantidad_1':'15', 'cantidad_2':'123'},
    {'nombre':'Empleado Dos',  'id':'12346', 'cantidad_1':'25', 'cantidad_2':'345'},
    {'nombre':'Empleado Tres', 'id':'12347', 'cantidad_1':'35', 'cantidad_2':'567'},
    {'nombre':'Empleado Cuatro', 'id':'12348', 'cantidad_1':'45', 'cantidad_2':'789'},
    ]


# fin.

