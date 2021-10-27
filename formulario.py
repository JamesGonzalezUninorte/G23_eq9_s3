from flask_wtf import FlaskForm
from flask_wtf.recaptcha import validators
from wtforms import PasswordField, SubmitField, TextField
# notafrom wtforms.fields.html5 import EmailField
from wtforms.validators import InputRequired, EqualTo

class pgLogin(FlaskForm):
    user=TextField('Ususario *', validators=[InputRequired()])
    passw=PasswordField('Contraseña *', validators=[InputRequired()])
    ingresar=SubmitField('Ingresar')
