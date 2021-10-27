from flask_wtf import FlaskForm
<<<<<<< HEAD
from flask_wtf.recaptcha import validators
from wtforms import PasswordField, SubmitField, TextField
# notafrom wtforms.fields.html5 import EmailField
from wtforms.validators import InputRequired, EqualTo

class pgLogin(FlaskForm):
    user=TextField('Ususario *', validators=[InputRequired()])
    passw=PasswordField('Contraseña *', validators=[InputRequired()])
    ingresar=SubmitField('Ingresar')
=======
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class FormInicio(FlaskForm):
    usuario = StringField('Usuario', validators=[DataRequired(message='No dejar vacío, completar')])
    contraseña = PasswordField('Contraseña', validators=[DataRequired(message='No dejar vacío, completar')])
    recordar = BooleanField('Recordar Usuario')
    correo = StringField('Correo', validators=[DataRequired(message='No dejar vacío, completar')])
    enviar = SubmitField('Iniciar Sesión')
>>>>>>> d0c3532fc8fa5cef78b29e3b2c78954435471dff
