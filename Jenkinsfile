pipeline {
    agent any
    stages {
        stage('Check file') {
            steps {
                sh '''
                  echo "📂 Files in repository:"
                    ls -al

                    echo "🔍 Checking for fruit_sales.xlsx..."
                    test -f fruit_sales.xlsx && echo "✅ File exists" || echo "❌ File not found"
                '''
            }
        }
    }
}