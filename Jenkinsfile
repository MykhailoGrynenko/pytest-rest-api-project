pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sh 'python3 --version'
                sh 'python3 virtualenv my_venv'
                sh 'python3 source my_venv/bin/activate'
                sh 'python3 pip install --upgrade pip'
                sh 'python3 pip install -r requirements.txt'
                sh 'python3 pytest -sv'
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