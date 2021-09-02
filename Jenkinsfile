pipeline {
    agent none
    stages {
        stage('build') {
            agent {
                docker {
                    image 'python:3.9.7-bullseye' 
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

