pipeline {
    agent { label 'playwright-node' }

    stages {

        stage('Checkout') {
            steps {
                git 'https://github.com/company/aws-alt-sso-automation.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install -r requirements.txt
                playwright install
                '''
            }
        }

        stage('Run Automation') {
            steps {
                sh '''
                . venv/bin/activate
                python src/main.py
                '''
            }
        }

    }
}
