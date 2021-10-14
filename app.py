from flask import Flask, render_template, request

app=Flask(__name__)

# nota 01
@app.route('/', methods=('GET', 'POST'))

# nota zz
# nota xx

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

