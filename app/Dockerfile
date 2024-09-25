FROM python:3.12-slim AS app

# Instala dependencias necesarias y MySQL
RUN apt-get update && apt-get install -y \
    gnupg \
    lsb-release \
    wget \
    && wget https://dev.mysql.com/get/mysql-apt-config_0.8.22-1_all.deb \
    && dpkg -i mysql-apt-config_0.8.22-1_all.deb \
    && apt-get update && apt-get install -y mysql-server \
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
