pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sh 'python3 -m venv my_venv'
                sh 'source my_venv/bin/activate'
                sh 'pip install -r requirements.txt'
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