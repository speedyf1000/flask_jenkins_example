pipeline {
    agent { docker { image 'python:3.9.7' } }
    stages {
        stage('build') {
            agent { docker { image 'python:3.9.7' } }
            steps {
                sh 'pip install flask'
            }
        }
        stage('test') {
            steps {
                sh 'python test.py'
            }
        }
    }
}

