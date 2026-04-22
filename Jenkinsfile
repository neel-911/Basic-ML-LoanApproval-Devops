pipeline {
    agent any

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
    }

    post {
        success {
            echo '=== Pipeline completed successfully! ==='
        }
        failure {
            echo '=== Pipeline failed! ==='
            mail to: 'neel2jaiswal@gmail.com',
                 subject: "FAILED: Pipeline ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                 body: "Pipeline failed. Check: ${env.BUILD_URL}"
        }
    }
}
