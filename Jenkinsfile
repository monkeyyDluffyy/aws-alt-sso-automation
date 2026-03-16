pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git 'https://github.com/monkeyyDluffyy/aws-alt-sso-automation.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                python3 -m venv venv
                source venv/bin/activate
                pip install -r requirements.txt
                playwright install
                '''
            }
        }

        stage('Run Automation') {
            steps {
                sh '''
                source venv/bin/activate
                python src/main.py
                '''
            }
        }
    }
}
