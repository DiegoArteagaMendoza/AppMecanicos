FROM python:latest

# Configura el directorio de trabajo
WORKDIR /app

# Copia los requisitos e instala las dependencias
COPY requirements.txt .
RUN pip3 --no-cache-dir install -r requirements.txt

# Copia todo el contenido del proyecto
COPY . .

# Expone el puerto 5000
EXPOSE 5000

# Configura la variable de entorno FLASK_APP
ENV FLASK_APP=src
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

# Ejecuta la aplicación Flask
CMD ["flask", "run", "--debug"]
