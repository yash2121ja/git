pipeline {
  agent any
  stages {
    stage('Step1') {
      steps {
        echo 'Pipeline started'
        sh '''sudo yum install python
'''
        echo 'python done'
      }
    }

    stage('') {
      steps {
        echo 'step 2'
        sh '''sudo pip install pylint
'''
      }
    }

  }
}