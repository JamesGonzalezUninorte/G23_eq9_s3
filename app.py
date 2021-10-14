'''Sprint 3
   Grupo 23 
   Equipo9
'''

from flask import Flask

def create_app():
    """
        fx Crear la aplicación principal

        Parametros: Ninguno

        Returns:    app de Flask

    """
    app=Flask(__name__)
    from views import main
    app.register_blueprint(main, url_prefix='/')
    return app
    
# fin.

