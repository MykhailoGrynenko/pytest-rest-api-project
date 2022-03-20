pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sh 'python3 -m venv my_venv'
                sh 'source my_venv/bin/activate'
                sh 'python3 pip install -r requirements.txt'
                sh 'pytest -sv'
                sh 'deactivate'
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