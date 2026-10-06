pipeline {
    agent none

    environment {
        IMAGE = 'ghcr.io/rmhzaal/docker-python-demo'
    }

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

        stage('Build and push') {
            agent any
            steps {
                sh 'docker build -t ${IMAGE}:jenkins-${GIT_COMMIT} .'
                withCredentials([usernamePassword(credentialsId: 'ghcr-credentials',
                                                  usernameVariable: 'GH_USER',
                                                  passwordVariable: 'GH_TOKEN')]) {
                    sh '''
                        echo "$GH_TOKEN" | docker login ghcr.io -u "$GH_USER" --password-stdin
                        docker push ${IMAGE}:jenkins-${GIT_COMMIT}
                    '''
                }
            }
            post {
                always {
                    sh 'docker logout ghcr.io || true'
                }
            }
        }
    }
}
