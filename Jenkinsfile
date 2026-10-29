
pipeline {
    agent any

    environment {
        DOCKERHUB_USER = 'sidaksingh1'
        IMAGE_NAME = 'multipage-app'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Images') {
            steps {
                script {
                    for (v in ['v1', 'v2', 'v3']) {
                        bat "docker build -t ${DOCKERHUB_USER}/${IMAGE_NAME}:${v} ${v}"
                    }
                }
            }
        }

        stage('Push to DockerHub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DH_USER',
                    passwordVariable: 'DH_PASS'
                )]) {
                    bat '''@echo off
echo %DH_PASS%| docker login -u %DH_USER% --password-stdin'''
                    script {
                        for (v in ['v1', 'v2', 'v3']) {
                            bat "docker push ${DOCKERHUB_USER}/${IMAGE_NAME}:${v}"
                        }
                    }
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                bat 'kubectl apply -f k8s/'
                bat 'kubectl rollout status deployment/multipage-v1 --timeout=180s'
                bat 'kubectl rollout status deployment/multipage-v2 --timeout=180s'
                bat 'kubectl rollout status deployment/multipage-v3 --timeout=180s'
                bat 'kubectl get deployments'
                bat 'kubectl get pods'
                bat 'kubectl get services'
            }
        }
    }

    post {
        success {
            echo 'Done! Open http://localhost:8084 (v1), http://localhost:8082 (v2), http://localhost:8083 (v3)'
        }
    }
}



