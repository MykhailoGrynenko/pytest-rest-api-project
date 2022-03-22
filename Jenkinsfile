pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sh """
                python3 -m venv my_venv
                source my_venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                pytest --alluredir=reports
                deactivate
                """
            }
        stage('Test') {
            steps {
            script {
                    allure([
                            includeProperties: false,
                            jdk: '',
                            properties: [],
                            reportBuildPolicy: 'ALWAYS',
                            results: [[path: 'reports']]
                    ])

            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}