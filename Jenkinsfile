pipeline {
  agent any
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
