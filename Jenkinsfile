pipeline {
    agent any

    environment {
        PYTHON_ENV = 'venv'
        FLASK_APP = 'app.py'
        GIT_REPO = 'https://github.com/qapacker/Jenkins.git'
    }

    stages {
        stage('Preparar') {
            steps {
                echo 'Clonando el repositorio y preparando el entorno'
                sh 'git clone $GIT_REPO .'

                script {
                    // Crear entorno virtual
                    sh 'python3 -m venv $PYTHON_ENV'
                    // Instalar dependencias
                    sh ". $PYTHON_ENV/bin/activate && pip install -r requirements.txt"
                }
            }
        }

        stage('Test') {
            steps {
                echo 'Ejecutando pruebas con pytest'
                script {
                    sh ". $PYTHON_ENV/bin/activate && pytest tests/"
                }
            }
        }

        stage('Desplegar') {
            steps {
                echo 'Desplegando la aplicación'
                script {
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
            echo 'Limpiando entorno virtual'
            sh 'rm -rf $PYTHON_ENV'
        }
    }
}
