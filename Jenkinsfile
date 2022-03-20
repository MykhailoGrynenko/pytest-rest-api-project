pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sh 'python3 --version'
                python3 -m venv my_venv
                source my_venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                pytest --alluredir=reports
                deactivate
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}