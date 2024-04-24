pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                // Checkout source code
                checkout scm

                // Build Docker image
                sh 'docker build -t django-session .'
            }
        }
        stage('Deploy') {
            steps {
                // Save Docker image
                sh 'docker save django-session -o django-session.tar'

                // Load Docker image
                sh 'docker load -i django-session.tar'

                // Stop current docker container
                sh 'docker ps -q --filter ancestor=django-session | xargs -r docker stop'
                sh 'docker ps -q --filter ancestor=django-session | xargs -r docker rm'

                // Run Docker container
                sh 'docker run -d -p 8000:8000 django-session'
            }
        }
    }
}