pipeline {
  agent any
  stages {
    stage('Step1') {
      steps {
        echo 'Pipeline started'
        sh '''pwd
ls
ls'''
      }
    }

    stage('step2') {
      steps {
        echo 'Starting git checkout process...'
        sh '''git checkout pipeline
commit
'''
      }
    }

  }
}
