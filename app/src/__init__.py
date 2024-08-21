from flask import Flask
import os

def create_app():
    app = Flask(__name__)
    app.config['UPLOAD_FOLDER'] = os.path.join('src', 'static', 'uploads')  # Carpeta para guardar los archivos
    app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

    # Importar y registrar las rutas
    with app.app_context():
        from .routes import init_routes
        init_routes(app)

    return app
