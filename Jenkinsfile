pipeline {
    agent any
    stages {
        stage('Check file') {
            steps {
                sh '''
                  if [test -f fruit_sales.xlsx];then
                    echo "File found"
                  else
                    echo "File not found"
                    exit 1
                  fi
                '''
            }
        }
    }
}