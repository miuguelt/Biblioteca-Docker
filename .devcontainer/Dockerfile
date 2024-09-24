# Usa una imagen base de Python
FROM python:3.12-slim AS app

# Establece el directorio de trabajo en el contenedor
WORKDIR /workspace

# Copia el contenido del directorio actual al directorio de trabajo en el contenedor
COPY ./app /workspace

# Instala las dependencias
RUN pip install -r requirements.txt

# Comando por defecto para ejecutar la aplicación
CMD ["python", "run1.py"]

# Usa una imagen base de MySQL
FROM mysql:9.0.1 AS db

# Establece las variables de entorno para MySQL
ENV MYSQL_DATABASE=flaskdb
ENV MYSQL_ROOT_PASSWORD=my-secret-pw

# Comando por defecto para ejecutar MySQL con las configuraciones especificadas
CMD ["mysqld", "--character-set-server=utf8mb4", "--collation-server=utf8mb4_unicode_ci", "--default-time-zone=+02:00"]
