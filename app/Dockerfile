FROM python:3.12-slim AS app

# Actualiza el sistema y instala las dependencias necesarias
RUN apt-get update && apt-get install -y \
    gnupg \
    lsb-release \
    wget \
    && wget https://dev.mysql.com/get/Downloads/MySQL-8.0/mysql-server_8.0.31-1ubuntu20.04_amd64.deb \
    && apt-get install -y ./mysql-server_8.0.31-1ubuntu20.04_amd64.deb \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Copia el archivo de configuración de MySQL
COPY /app/my.cnf /etc/mysql/my.cnf

# Copia el script de inicialización
COPY /app/init.sql /docker-entrypoint-initdb.d/

# Establece el directorio de trabajo en el contenedor
WORKDIR /workspace

# Copia solo requirements.txt primero para aprovechar la caché de Docker
COPY /app/requirements.txt .

# Instala las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del contenido del directorio actual al directorio de trabajo en el contenedor
COPY /app/ .

# Expone los puertos necesarios
EXPOSE 80 3306

# Inicializa MySQL y luego ejecuta tu aplicación
CMD service mysql start && mysql -e "CREATE DATABASE IF NOT EXISTS mydatabase;" && python run1.py
