pipeline {
    agent any
    stages {
        stage('Check file') {
            steps {
                sh '''
                  echo "📂 Files in repository:"
                    ls -al
                  TODAY=$(TZ="America/Chicago" date +%Y%m%d)
                  FILE="fruit_sales_${TODAY}.xlsx"
                  echo "The file name I'm looking for is: $FILE"
                  echo "🔍 Checking for fruit_sales.xlsx..."
                  test -f "$FILE" && echo "✅ File exists for today" || echo "❌ File not found.."
                '''
            }
        }
    }
}