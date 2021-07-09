pipeline {
  agent any
  stages {
    stage('Step1') {
      steps {
        echo 'Pipeline started'
        sh '''sudo pip install pylint
ls
python -m pylint queue.py'''
      }
    }

  }
}