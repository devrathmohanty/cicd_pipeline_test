pipeline {
  agent { docker { image 'python:3.5.2'}}
  stages {
    stage('build') {
      steps {
        echo "building the application"
        sh 'pip install -r requirements.txt'
      }
    }
    stage('test') {
      steps {
        echo "testing the application"
        sh 'python test.py'
      }
      post {
        always {
          junit 'test-reports/*.xml'
        }
      }
    }
  }
}
