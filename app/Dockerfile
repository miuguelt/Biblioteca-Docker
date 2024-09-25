# Usa una imagen base de Python
FROM python:3.12-slim AS app

RUN apt-get update && apt-get install -y gnupg \
    && apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 5072E1F5


# Copia el archivo de configuración de MySQL
COPY /app/my.cnf /etc/mysql/my.cnf

# Copia el script de inicialización
COPY /app/init.sql /docker-entrypoint-initdb.d/

# Establece el directorio de trabajo en el contenedor
WORKDIR /workspace

# Copia solo requirements.txt primero para aprovechar la caché de Docker
COPY /app/requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del contenido del directorio actual al directorio de trabajo en el contenedor
COPY /app/ .

# Expone el puerto 80 y 3306
EXPOSE 80 3306

# Configura MySQL y luego inicia la aplicación
CMD service mysql start && mysqld_safe && python run1.py

