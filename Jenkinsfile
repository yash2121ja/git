pipeline {
  agent any
  stages {
    stage('Step1') {
      steps {
        echo 'Pipeline started'
        sh '''pwd
ls
rm -rf .git
git clone https://github.com/yash2121ja/git.git
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
