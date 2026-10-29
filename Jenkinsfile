
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'GitHub checkout completed by Jenkins'
            }
        }

        stage('Verify Project') {
            steps {
                echo 'Jenkins pipeline is running successfully'
                sh 'ls -la'
            }
        }
    }
}

