pipeline {
  agent any
  stages {
    stage('Step1') {
      steps {
        echo 'Pipeline started'
        sh 'pip install pylint'
        echo 'python done'
      }
    }

    stage('error') {
      steps {
        echo 'step 2'
        sh '''sudo pip install pylint
'''
      }
    }

  }
}