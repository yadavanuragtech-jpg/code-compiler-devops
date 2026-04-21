pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/yadavanuragtech-jpg/code-compiler-devops.git'
            }
        }

        stage('Build Backend Docker Image') {
            steps {
                sh 'docker build -t compiler-backend ./backend'
            }
        }

        stage('Build Frontend Docker Image') {
            steps {
                sh 'docker build -t compiler-frontend ./frontend'
            }
        }

        stage('Run Containers') {
            steps {
                sh 'docker stop backend || true'
                sh 'docker stop frontend || true'
                sh 'docker rm backend || true'
                sh 'docker rm frontend || true'

                sh 'docker run -d -p 5000:5000 --name backend compiler-backend'
                sh 'docker run -d -p 3000:80 --name frontend compiler-frontend'
            }
        }
    }
}
