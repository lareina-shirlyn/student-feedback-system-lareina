pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t feedback-app .'
            }
        }

        stage('Stop Old Container') {
            steps {
                sh 'docker stop feedback || true'
                sh 'docker rm feedback || true'
            }
        }

        stage('Run New Container') {
            steps {
                sh 'docker run -d -p 5000:5000 --name feedback feedback-app'
            }
        }
    }
}
