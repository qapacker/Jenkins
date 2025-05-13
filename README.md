# Repo para EU - DevOps&Cloud - UNIR

Este repositorio incluye un proyecto sencillo para demostrar los conceptos de pruebas unitarias, pruebas de servicio, uso de Wiremock y pruebas de rendimiento
El objetivo es que el alumno entienda estos conceptos, por lo que el código y la estructura del proyecto son especialmente sencillos.
Este proyecto sirve también como fuente de código para el pipeline de Jenkins.

## Proyecto API Flask con Docker

Este proyecto implementa una API en Python utilizando Flask para realizar operaciones matemáticas. Está configurado para ejecutarse en Docker, lo que facilita su despliegue y ejecución en cualquier entorno.

### Requisitos

- Docker  
- Docker Compose

## Instrucciones para Ejecutar

## Clonar el repositorio
git clone <URL_DEL_REPOSITORIO>
cd <nombre_del_repositorio>

## Construir la imagen Docker
docker build -t my-flask-api .

## Levantar el contenedor en segundo plano
docker-compose up --build -d

## Mensaje de éxito
echo "La API está corriendo en http://localhost:5000"

## Mostrar los endpoints disponibles
"Endpoints disponibles:"
"Suma: GET /calc/add/{op1}/{op2}"
"Resta: GET /calc/substract/{op1}/{op2}"
"Multiplicación: GET /calc/multiply/{op1}/{op2}"
"División: GET /calc/divide/{op1}/{op2}"


# Configuración de Jenkins

1. **Iniciar Jenkins:**
   Una vez que el contenedor de Jenkins esté en ejecución, accede a Jenkins en [http://localhost:8080](http://localhost:8080).

2. **Configurar Pipeline de Jenkins:**
   El pipeline de Jenkins está preparado para ejecutar tareas de construcción, pruebas y despliegue del proyecto de manera automática.

3. **Volúmenes de Jenkins:**
   Los datos de Jenkins se almacenan en un volumen persistente (`jenkins_home`), lo que garantiza que la configuración y los datos se mantengan entre reinicios del contenedor.