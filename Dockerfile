FROM python:latest

WORKDIR /app

COPY requirements.txt .
RUN pip3 --no-cache-dir install -r requirements.txt


COPY . .

EXPOSE 5000

CMD [ "flask", "--app", "src", "run", "--debug", "--host=0.0.0.0"]

# FROM python:latest

# EXPOSE 7000

# WORKDIR app

# COPY * /app/

# RUN pip install -r requirements.txt

# CMD python app.py
# FROM python:latest

# WORKDIR /app

# COPY requirements.txt requirements.txt
# RUN pip3 --no-cache-dir install -r requirements.txt

# COPY . .

# CMD ["python3", "src/app.py"]