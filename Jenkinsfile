pipeline {
  agent any
  stages {
    stage('Step1') {
      steps {
        echo 'Pipeline started'
        sh '''git pull 
ls'''
        echo 'python done'
      }
    }

    stage('error') {
      steps {
        echo 'step 2'
        sh 'python3 -m pylint deploy.py'
      }
    }

  }
}