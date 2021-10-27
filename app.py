"""Sprint 3
   Grupo 23 
   Equipo 9
"""
import os
from flask import Flask, blueprints

def create_app():
    """fx Crear la aplicación principal

       Parametros: Ninguno
       Returns:    app de Flask
    """

    app=Flask(__name__)
    app.secret_key = os.urandom(19)
    from views import main
    app.register_blueprint(main, url_prefix='/')

    return app
    
# fin.

