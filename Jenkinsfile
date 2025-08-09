pipeline {
    agent any
    environment {
        TODAY=$(TZ="America/Chicago" date +%Y%m%d)
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
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
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