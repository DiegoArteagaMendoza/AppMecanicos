from flask import render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import json, os, random

def init_routes(app):

    @app.route('/')
    def home():
        return render_template("index.html")

    @app.route('/Servicios')
    def servicios():
        clients, vehiculos, servicios, imagenes = cargar_datos()
        return render_template("servicios.html", servicios=servicios, imagenes = imagenes)

    @app.route('/Trabajos')
    def trabajos():
        clients, vehiculos, servicios, imagenes = cargar_datos()
        return render_template("trabajos.html", clients=clients, vehiculos=vehiculos, servicios = servicios)

    @app.route('/AgregarTrabajo')
    def formAddTrabajo():
        _, _, servicios, _ = cargar_datos()
        return render_template("addtrabajo.html", servicios = servicios)

    @app.route('/addTrabajo', methods=['POST'])
    def addTrabajo():
        id_cliente = random.random()
        client = {
            "name": request.form['name'],
            "rut": request.form['rut'],
            "phone": '+56' + request.form['phone'],
            "email": request.form['email'],
            "date": request.form['date'],
            "id": id_cliente
        }

        vehiculo = {
            "type": request.form['tipo'],
            "marca": request.form['marca'],
            "patente": request.form['patente'],
            "modelo": request.form['modelo'],
            "OpcionesTrabajo": request.form['OpcionesTrabajo'],
            "motivo": request.form['motivo'],
            "id": id_cliente
        }

        guardar_datos_cliente_vehiculo(client, vehiculo)
        return redirect(url_for('trabajos'))
    
    @app.route('/admin/Agregarservicio')
    def formAddServicio():
        return render_template("addservicio.html")

    @app.route('/addServicio', methods=['POST'])
    def addServicio():
        if 'img' not in request.files:
            return redirect(request.url)
        
        file = request.files['img']

        if file.filename == '':
            return redirect(request.url)
        
        if file and allowed_file(file.filename):
            # Generar un ID único para el servicio
            id_servicio = str(random.randint(10000, 99999))
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            
            # Asegúrate de que la carpeta de uploads exista
            if not os.path.exists(app.config['UPLOAD_FOLDER']):
                os.makedirs(app.config['UPLOAD_FOLDER'])

            file.save(file_path)

            servicio = {
                "name": request.form['name'],
                "descripcion": request.form['descripcion'],
                "tiempo": request.form['tiempo'],
                "valor": request.form['valor'],
                "id": id_servicio
            }

            imagen = {
                "img": filename,
                "id": id_servicio
            }

            guardar_servicio(servicio, imagen)
            return redirect(url_for('servicios'))
        
        return redirect(request.url)

    def cargar_datos():
        if os.path.exists('clients.json'):
            with open('clients.json', 'r') as file:
                clients = json.load(file)
        else:
            clients = []

        if os.path.exists('vehiculos.json'):
            with open('vehiculos.json', 'r') as file:
                vehiculos = json.load(file)
        else:
            vehiculos = []

        if os.path.exists('servicios.json'):
            with open('servicios.json', 'r') as file:
                servicios = json.load(file)
        else:
            servicios = []

        if os.path.exists('imagenes.json'):
            with open('imagenes.json', 'r') as file:
                imagenes = json.load(file)
        else:
            imagenes = []

        return clients, vehiculos, servicios, imagenes

    def guardar_datos_cliente_vehiculo(client, vehiculo):
        clients, vehiculos, _, _ = cargar_datos()

        clients.append(client)
        vehiculos.append(vehiculo)

        with open('clients.json', 'w') as file:
            json.dump(clients, file, indent=4)

        with open('vehiculos.json', 'w') as file:
            json.dump(vehiculos, file, indent=4)

    def guardar_servicio(servicio, imagen):
        _, _, servicios, imagenes = cargar_datos()
        
        servicios.append(servicio)
        imagenes.append(imagen)

        with open('servicios.json', 'w') as file:
            json.dump(servicios, file, indent=4)
        
        with open('imagenes.json', 'w') as file:
            json.dump(imagenes, file, indent=4)

    def allowed_file(filename):
        return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']
