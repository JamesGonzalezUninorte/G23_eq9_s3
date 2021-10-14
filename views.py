'''Sprint 3
   Grupo 23 
   Equipo9
'''

from flask import Flask, render_template, blueprints, request, redirect, url_for, jsonify


lst_Empleados=[
    {'nombre':'Empleado Uno',  'id':'12345', 'cantidad_1':'15', 'cantidad_2':'123'},
    {'nombre':'Empleado Dos',  'id':'12346', 'cantidad_1':'25', 'cantidad_2':'345'},
    {'nombre':'Empleado Tres', 'id':'12347', 'cantidad_1':'35', 'cantidad_2':'567'},
    {'nombre':'Empleado Cuatro', 'id':'12348', 'cantidad_1':'45', 'cantidad_2':'789'},
    ]

# nota 01
@main.route('/', methods=('GET', 'POST')
def ():
    '''
    '''
    return render_templete('')

# nota nota xx

# nota 02
@app.route('/login/', methods=('GET', 'POST'))

# nota 03
@app.route('/empleado', methods=('GET', 'POST'))

# nota 04
@app.route('/retroalimentacion', methods=('GET', 'POST'))

# nota 05
@app.route('/dashboard_adm', methods=('GET', 'POST'))

# nota 06
@app.route('/eliminar', methods=('GET', 'POST'))

# nota 07
@app.route('/crear', methods=('GET', 'POST'))

# nota 08
@app.route('/editar', methods=('GET', 'POST'))
def editar():
    return render_template("pg08.html")

# fin.

