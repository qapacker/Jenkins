
# 🧪 Proyecto DevOps & Cloud - UNIR

Este repositorio contiene un proyecto sencillo diseñado para demostrar conceptos fundamentales relacionados con:

- ✅ Pruebas unitarias  
- ✅ Pruebas de servicio  
- ✅ Uso de **Wiremock**  
- ✅ Pruebas de rendimiento  
- ✅ Integración en un **pipeline de Jenkins**

> El objetivo principal es **facilitar el aprendizaje** de estos conceptos, por lo que el código ha sido intencionadamente simplificado.

---

## 📦 Proyecto API Flask con Docker

Este proyecto implementa una API RESTful utilizando **Python + Flask** para realizar operaciones matemáticas básicas. Se encuentra **dockerizado**, lo que facilita su despliegue en distintos entornos y su integración en un pipeline CI/CD con Jenkins.

---

## 📚 Tabla de Contenidos

- [Requisitos](#requisitos)
- [Instalación y Ejecución](#instalación-y-ejecución)
- [Uso de la API](#uso-de-la-api)
- [Integración con Jenkins](#integración-con-jenkins)
- [Características](#características)
- [Dependencias](#dependencias)
- [Configuración](#configuración)
- [Ejemplos](#ejemplos)
- [Contribuidores](#contribuidores)
- [Licencia](#licencia)

---

## ✅ Requisitos

Antes de comenzar, asegúrate de tener instalado lo siguiente:

- Docker
- Docker Compose
- Git

---

## 🛠️ Instalación y Ejecución

### 1. Clona el repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
cd <nombre_del_repositorio>
```

### 2. Construye la imagen Docker

```bash
docker build -t my-flask-api .
```

### 3. Levanta los contenedores con Docker Compose

```bash
docker-compose up --build -d
```

### 4. Verifica que la API esté funcionando

```bash
echo "La API está corriendo en http://localhost:5000"
```

---

## 🚀 Uso de la API

### Endpoints disponibles:

- ➕ **Suma:** GET /calc/add/{op1}/{op2}
- ➖ **Resta:** GET /calc/substract/{op1}/{op2}
- ✖️ **Multiplicación:** GET /calc/multiply/{op1}/{op2}
- ➗ **División:** GET /calc/divide/{op1}/{op2}

---

## 🔧 Integración con Jenkins

### 1. Iniciar Jenkins

Asegúrate de tener un contenedor de Jenkins en funcionamiento. Accede desde:

http://localhost:8080

### 2. Configurar Pipeline

- El pipeline está preparado para realizar:
  - Construcción del proyecto
  - Ejecución de pruebas unitarias y de servicio
  - Despliegue automático de la aplicación

### 3. Volúmenes Persistentes

Los datos de Jenkins se almacenan en un volumen (`jenkins_home`) para conservar la configuración entre reinicios.

### 4. Configuración de Agentes

Antes de ejecutar el pipeline con agentes:

- Configura los agentes desde el nodo **master** en Jenkins.
- Añade el **secret key** correspondiente en las variables de entorno de cada agente para permitir la conexión.
- Asegúrate de que todos los contenedores estén en la **misma red Docker** para permitir la comunicación.

---

## ✨ Características

- API RESTful simple en Flask
- Pruebas unitarias y de servicio integradas
- Soporte para pruebas con Wiremock
- Desplegable vía Docker y Docker Compose
- Pipeline de CI/CD automatizado con Jenkins

---

## 📦 Dependencias

- Python 3.8+
- Flask
- pytest
- Wiremock (para pruebas de servicio)
- Docker / Docker Compose
- Jenkins

---

## ⚙️ Configuración

- Las variables de entorno relevantes deben configurarse en los contenedores de Jenkins y la API si es necesario.
- Asegúrate de exponer correctamente los puertos:
  - API: 5000
  - Jenkins: 8080

---

## 🧪 Ejemplos

```bash
curl http://localhost:5000/calc/add/10/5
# Resultado: {"operation": "add", "result": 15}
```

---

## 📝 Licencia

Distribuido bajo licencia educativa para uso no comercial y académico.
