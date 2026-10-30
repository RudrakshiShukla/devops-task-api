
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Source code checked out from GitHub'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip3 install --break-system-packages -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'python3 -m unittest test_app -v'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                    docker build -t devops-task-api:${BUILD_NUMBER} .
                    docker tag devops-task-api:${BUILD_NUMBER} devops-task-api:latest
                '''
            }
        }

        stage('Verify Project') {
            steps {
                sh 'ls -la'
            }
        }
    }
}
