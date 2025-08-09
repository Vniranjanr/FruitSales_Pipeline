pipeline {
    agent any
    stages {
        stage('Check file') {
            steps {
                sh '''
                  echo "📂 Files in repository:"
                    ls -al

                    echo "🔍 Checking for fruit_sales.xlsx..."
                    test -f fruit_sales.xlsx && echo "✅ File exists" || echo "❌ File not found.."

                    TODAY=$(TZ="America/Chicago" date +%Y%m%d)
                    FILE="fruit_sales_${TODAY}.xlsx"
                    echo "The file name I'm looking for is: $FILE"
                '''
            }
        }
    }
}