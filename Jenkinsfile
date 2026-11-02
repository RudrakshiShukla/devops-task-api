
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
                    docker build -t shuklarudrakshi/devops-task-api:${BUILD_NUMBER} .
                    docker tag shuklarudrakshi/devops-task-api:${BUILD_NUMBER} shuklarudrakshi/devops-task-api:latest
                '''
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-credentials',
                    usernameVariable: 'DOCKERHUB_USER',
                    passwordVariable: 'DOCKERHUB_TOKEN'
                )]) {
                    sh '''
                        printf '%s' "$DOCKERHUB_TOKEN" | docker login --username "$DOCKERHUB_USER" --password-stdin

                        docker push shuklarudrakshi/devops-task-api:${BUILD_NUMBER}
                        docker push shuklarudrakshi/devops-task-api:latest

                        docker logout
                    '''
                }
            }
        }

        stage('Deploy Application') {
            steps {
                sh '''
                    docker pull shuklarudrakshi/devops-task-api:${BUILD_NUMBER}

                    docker rm -f task-api-deployed || true

                    docker run -d \
                    --name task-api-deployed \
                    -p 5001:5000 \
                    shuklarudrakshi/devops-task-api:${BUILD_NUMBER}
                '''
            }
        }

       
stage('Health Check') {
    steps {
        sh '''
            echo "Checking application health..."

            for i in $(seq 1 10); do
                if docker exec task-api-deployed python3 -c "import urllib.request; urllib.request.urlopen('http://localhost:5000/health', timeout=5)" ; then
                    echo "Application is healthy!"
                    exit 0
                fi

                echo "Waiting for application..."
                sleep 3
            done

            echo "Health check failed!"
            exit 1
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
