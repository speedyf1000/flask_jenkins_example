pipeline {
    agent any
    stages {
        stage('build') {
            agent {
                docker {
                    image 'python:3-alpine' 
                } 
            }
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

