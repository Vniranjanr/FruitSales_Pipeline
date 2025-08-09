pipeline {
    agent any
    environment {
        TODAY = "${new Date().format('yyyyMMdd', TimeZone.getTimeZone('America/Chicago'))}"
        FILE="fruit_sales_${TODAY}.xlsx"
    }
    stages {
        stage('Check file') {
            steps {
                sh '''
                  echo "🔍 Checking for today's file..."
                  test -f "$FILE" && echo "✅ File exists for today" || echo "❌ File not found.."
                '''
            }
        }
        stage('Check for blanks in Excel') {
            agent {
                docker {
                    image 'python:3.10-slim'  // or any python image you prefer
                    args '-v $WORKSPACE:$WORKSPACE -w $WORKSPACE'  // mount workspace
                }
            }
            steps {
                sh '''
                    pip install pandas openpyxl
                    python - <<EOF
import os
import pandas as pd

FILE = os.getenv('FILE')
if not FILE:
    print("FILE environment variable not set")
    exit(1)

df = pd.read_excel(FILE)
if df.isnull().values.any():
    print("blanks found")
else:
    print("no blanks found")
EOF
                '''
            }
        }
    }
}