FROM python:3.12-slim AS app

# Instala las dependencias necesarias para MySQL
RUN apt-get update && apt-get install -y \
    gnupg \
    wget \
    lsb-release \
    && wget https://dev.mysql.com/get/mysql-apt-config_0.8.22-1_all.deb \
    && dpkg -i mysql-apt-config_0.8.22-1_all.deb \
    && apt-get update \
    && apt-get install -y mysql-server \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copia el archivo de configuración de MySQL (si lo tienes)
COPY /app/my.cnf /etc/mysql/my.cnf

# Copia el script de inicialización (si lo tienes)
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

# Comando para iniciar MySQL y luego la aplicación
CMD service mysql start && python run1.py
