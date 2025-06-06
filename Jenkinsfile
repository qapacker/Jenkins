pipeline {
    agent none

    environment {
        PYTHON_ENV = 'venv'
        GIT_REPO   = 'https://github.com/qapacker/Jenkins.git'
    }

    stages {
        stage('Preparar') {
            agent any
            steps {
                echo '🔄 Limpiando workspace'
                sh 'find . -mindepth 1 -maxdepth 1 -exec rm -rf {} +'
                echo '🔗 Clonando repositorio'
                sh "git clone ${GIT_REPO} ."
                stash includes: '**', name: 'source_code'
            }
        }

        stage('Test') {
            agent { label 'agent-1' }
            steps {
                echo '📥 Recuperando código'
                unstash 'source_code'

                echo '🛠️ Configurando entorno Python'
                sh '''
                  bash -lc "
                    python3 -m venv ${PYTHON_ENV} &&
                    source ${PYTHON_ENV}/bin/activate &&
                    pip install --upgrade pip &&
                    pip install --no-cache-dir -r requirements.txt
                  "
                '''

                echo '🚀 Arrancando API Flask en background'
                sh '''
                  bash -lc "
                    source ${PYTHON_ENV}/bin/activate &&
                    nohup python app/api.py > flask.log 2>&1 &
                    sleep 3
                  "
                '''

                echo '✅ Ejecutando pytest contra localhost:5000'
                sh '''
                  bash -lc "
                    source ${PYTHON_ENV}/bin/activate &&
                    export PYTHONPATH=$(pwd) &&
                    export BASE_URL=http://localhost:5000 &&
                    pytest test/
                  "
                '''
            }
        }

        stage('Desplegar') {
            agent { label 'agent-2' }
            steps {
                echo '📥 Recuperando código'
                unstash 'source_code'

                echo '🐳 Construyendo imagen Docker'
                sh 'docker build -t myapp .'

                echo '🚀 Lanzando contenedor'
                sh 'docker run -d -p 7000:5000 myapp'
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline exitoso'
        }
        failure {
            echo '❌ Pipeline fallido'
        }
    }
}
