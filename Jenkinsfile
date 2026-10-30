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

        stage('Verify Project') {
            steps {
                sh 'ls -la'
            }
        }
    }
}

