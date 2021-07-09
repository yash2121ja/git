pipeline {
  agent any
  stages {
    stage('Step1') {
      steps {
        echo 'Pipeline started'
        sh '''pwd
ls
git pull
ls'''
      }
    }

    stage('step2') {
      steps {
        sh '''python3 -m pylint queue.py
'''
      }
    }

  }
}