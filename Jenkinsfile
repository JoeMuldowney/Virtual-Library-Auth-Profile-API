pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = '95d202ba-9223-45f8-8531-bfe1eb84c3d2'
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
                    sh 'docker tag vlibrarybackend joemuldowney/virtual_library_auth'

                    // Push Docker image to Docker Hub
                    sh 'docker push joemuldowney/virtual_library_auth'
           }
          }
        }
        stage('Deploy') {
            steps {
            sh 'docker run -d -p 8000:8000 --name vlibrarybackend joemuldowney/virtual_library_auth'
            }
        }
    }
}