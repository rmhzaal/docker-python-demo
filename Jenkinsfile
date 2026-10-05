pipeline {
    agent any

    stages {
        stage('Test') {
            agent {
                docker { image 'python:3.11-slim' }
            }
            steps {
                sh '''
                    python -m venv .venv
                    . .venv/bin/activate
                    pip install -r requirements.txt -r requirements-dev.txt
                    pytest -v
                '''
            }
        }

        stage('Build image') {
            steps {
                sh 'docker build -t docker-python-demo:${GIT_COMMIT} .'
            }
        }
    }
}
