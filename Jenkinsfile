pipeline {
    agent any

    environment {
        PYTHON_ENV = 'venv'
        FLASK_APP = 'app.py'
        GIT_REPO = 'https://github.com/qapacker/Jenkins.git'
        BASE_URL = "http://jenkins-app-1:5000"
        PYTHONPATH = '/var/jenkins_home/workspace/cp1'
    }

    stages {
        stage('Preparar') {
            steps {
                echo 'Limpiando el workspace y preparando el entorno'
                deleteDir() // Limpiar el workspace completamente
                sh "git clone $GIT_REPO ." // Clonar el repositorio

                script {
                    // Crear entorno virtual e instalar dependencias
                    sh "python3 -m venv $PYTHON_ENV"
                    sh "bash -c 'source $PYTHON_ENV/bin/activate && pip install -r requirements.txt'"
                }
            }
        }

        stage('Test') {
            steps {
                echo 'Ejecutando pruebas con pytest'
                script {
                    // Ejecutar las pruebas directamente sobre la API ya disponible
                    sh "bash -c 'source $PYTHON_ENV/bin/activate && PYTHONPATH=$PYTHONPATH pytest test/'"
                }
            }
        }

        stage('Desplegar') {
            steps {
                echo 'Desplegando la aplicación'
                script {
                    // Si necesitas volver a desplegar la app, asegúrate de que este paso sea necesario
                    sh 'docker build -t myapp .'
                    sh 'docker run -d -p 6000:6000 myapp'
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
            echo 'Limpiando entorno virtual'
            sh "rm -rf $PYTHON_ENV"
        }
    }
}
