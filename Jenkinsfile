pipeline {
    agent any

    environment {
        PATH = "/usr/local/bin:/opt/homebrew/bin:${env.PATH}"
    }

    stages {
        stage('Checkout') {
            steps {
                echo '=== Checking out source code ==='
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                echo '=== Installing dependencies ==='
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Build') {
            steps {
                echo '=== Running Loan Approval App ==='
                sh 'python3 app.py'
            }
        }

        stage('Test') {
            steps {
                echo '=== Running Tests ==='
                sh 'python3 -m pytest test_app.py -v'
            }
        }

        stage('Docker Build') {
            steps {
                echo '=== Building Docker Image ==='
                sh 'docker build -t loan-approval-app .'
            }
        }

        stage('Docker Run') {
            steps {
                echo '=== Running Docker Container ==='
                sh 'docker run --rm loan-approval-app'
            }
        }
    }

    post {
        success {
            echo '=== Pipeline completed successfully! ==='
        }
        failure {
            echo '=== Pipeline failed! ==='
        }
    }
}
