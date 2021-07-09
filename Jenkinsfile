pipeline {
  agent any
  stages {
    stage('Step1') {
      steps {
        echo 'Pipeline started'
        sh '''sh \'sudo pip install pylint\'
ls
sh \'python -m pylint queue.py\''''
      }
    }

  }
}