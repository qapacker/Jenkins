pipeline {
    agent any  // Usamos cualquier agente disponible

    environment {
        PYTHON_ENV = 'venv'  // Nombre del entorno virtual que se creará
        FLASK_APP = 'app.py'  // Nombre de la aplicación Flask
    }

    stages {
        stage('Preparar') {
            steps {
                echo 'Clonando el repositorio y preparando el entorno'
                checkout scm  // Clona el repositorio
                script {
                    // Crear un entorno virtual y activar
                    sh 'python3 -m venv $PYTHON_ENV'
                    sh '. $PYTHON_ENV/bin/activate'
                    // Instalar dependencias desde el archivo requirements.txt
                    sh 'pip install -r requirements.txt'
                }
            }
        }

        stage('Test') {
            steps {
                echo 'Ejecutando pruebas con pytest'
                script {
                    // Activar el entorno virtual y ejecutar pytest
                    sh '. $PYTHON_ENV/bin/activate'
                    sh 'pytest tests/'  // Directorio de tus pruebas
                }
            }
        }

        stage('Desplegar') {
            steps {
                echo 'Desplegando la aplicación'
                script {
                    // Aquí puedes ejecutar el despliegue, por ejemplo, con Docker
                    // Si tienes un Dockerfile, puedes construir y correr el contenedor
                    sh 'docker build -t myapp .'
                    sh 'docker run -d -p 5000:5000 myapp'
                }
            }
        }
    }

    post {
        success {
            echo 'El pipeline ha sido exitoso'
        }
        failure {
            echo 'El pipeline ha fallado'
        }
        always {
            // Limpiar cualquier recurso, como el entorno virtual
            sh 'rm -rf $PYTHON_ENV'
        }
    }
}