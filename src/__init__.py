from flask import Flask

def create_app():
    app = Flask(__name__)

    # Importar y registrar las rutas
    with app.app_context():
        from .app import init_routes
        init_routes(app)

    return app