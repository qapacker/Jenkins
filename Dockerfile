# Usa una imagen oficial de Python
FROM python:3.12-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia los archivos necesarios
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código
COPY . .

# Expone el puerto en el que corre la app Flask
EXPOSE 5000

# Comando para ejecutar la aplicación Flask desde la carpeta 'app'
CMD ["python", "app/api.py"]
