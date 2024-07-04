pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = '95d202ba-9223-45f8-8531-bfe1eb84c3d2'
        DB_NAME = credentials('2fef0c53-32ee-4099-bbf6-c3b2722e572c')
        DB_USER = credentials('0d5c1b71-fa2b-409d-a59d-019ece485a1a')
        DB_PASS = credentials('95b75b27-550a-460a-8b9a-3c6f742b3e63')
        DB_HOST = credentials('d35f73eb-6209-402a-8d48-3173464d25a9')
        SECRET_KEY = credentials('4703708b-ce88-4e96-b358-4a19335d821b')
    }
    stages {
        stage('Remove old build'){
            steps{
        // Stop and remove current docker container to free up space
                sh 'docker stop vlibrarybackend || true'
                sh 'docker rm vlibrarybackend || true'
                sh 'docker system prune -af'
            }
        }
        stage('Build') {
            steps {
                // Checkout source code
                checkout scm

                // Build Docker image
                sh 'docker build -t vlibrarybackend .'
            }
        }
        stage('Push to Docker Hub') {
            steps {

            withCredentials([usernamePassword(credentialsId: DOCKERHUB_CREDENTIALS, usernameVariable: 'DOCKERHUB_USERNAME', passwordVariable: 'DOCKERHUB_PASSWORD')])
           {
                    sh 'docker login -u $DOCKERHUB_USERNAME -p $DOCKERHUB_PASSWORD'

                    // Tag Docker image
                    sh 'docker tag vlibrarybackend joemuldowney/djangoauth'

                    // Push Docker image to Docker Hub
                    sh 'docker push joemuldowney/djangoauth'
           }
          }
        }
        stage('Deploy') {
            steps {
            sh 'docker run -d -p 8000:8000 --name vlibrarybackend joemuldowney/djangoauth'
            }
        }
    }
}