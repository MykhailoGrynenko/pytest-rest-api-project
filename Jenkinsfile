pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sh 'python3 --version'
                virtualenv my_venv
                source my_venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                pytest -sv
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