# DevOps Task API

A Python Flask application demonstrating an end-to-end CI/CD pipeline using **Git, GitHub, Jenkins, Docker, and Docker Hub**.

The pipeline automates code checkout, dependency installation, unit testing, Docker image building, image publishing, application deployment, and health checks.

## Tech Stack
- Python (Flask)
- Git & GitHub
- Jenkins
- Docker
- Docker Hub
- Python Unittest

## Key Features
- Automated CI/CD pipeline
- Automated unit testing
- Docker image creation and publishing
- Containerized application deployment
- Automated application health checks



## CI/CD Pipeline

1. Developer pushes code to GitHub.
2. Jenkins detects the changes through SCM polling.
3. Dependencies are installed.
4. Unit tests are executed.
5. Docker image is built and pushed to Docker Hub.
6. The application is deployed in a Docker container.
7. An automated health check verifies the deployment.

## Run Locally

1. Clone the repository:
   `git clone https://github.com/RudrakshiShukla/devops-task-api.git`

2. Navigate to the project:
   `cd devops-task-api`

3. Install dependencies:
   `pip install -r requirements.txt`

4. Run the application:
   `python app.py`

5. Open: `http://localhost:5000`

## API Endpoints

- `/` – Task dashboard
- `/tasks` – Returns task data in JSON
- `/health` – Application health status