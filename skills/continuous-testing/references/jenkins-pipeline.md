# Jenkins Pipeline

## Jenkins Pipeline

```groovy
// Jenkinsfile
pipeline {
    agent any

    environment {
        NODE_VERSION = '18'
        DATABASE_URL = credentials('test-database-url')
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'npm ci'
            }
        }

        stage('Parallel Tests') {
            parallel {
                stage('Unit Tests') {
                    steps {
                        sh 'npm run test:unit -- --coverage'
                    }
                    post {
                        always {
                            junit 'test-results/junit.xml'
                            publishCoverage adapters: [
                                coberturaAdapter('coverage/cobertura-coverage.xml')
                            ]
                        }
                    }
                }

                stage('Integration Tests') {
                    steps {
                        sh 'npm run test:integration'
                    }
                }

                stage('Lint & Type Check') {
                    steps {
                        sh 'npm run lint'
                        sh 'npm run type-check'
                    }
                }
            }
        }

        stage('E2E Tests') {
            steps {
                sh 'npx playwright install --with-deps'
                sh 'npm run build'
                sh 'npx playwright test'
            }
            post {
                always {
                    publishHTML([
                        reportDir: 'playwright-report',
                        reportFiles: 'index.html',
                        reportName: 'Playwright Report'
                    ])
                }
            }
        }

        stage('Security Scan') {
            steps {
                sh 'npm audit --audit-level=high'
                sh 'npx snyk test --severity-threshold=high'
            }
        }

        stage('Quality Gate') {
            steps {
                script {
                    def coverage = readFile('coverage/coverage-summary.json')
                    def coverageData = new groovy.json.JsonSlurper().parseText(coverage)
                    def lineCoverage = coverageData.total.lines.pct

                    if (lineCoverage < 80) {
                        error "Coverage ${lineCoverage}% is below threshold 80%"
                    }
                }
            }
        }

        stage('Deploy to Staging') {
            when {
                branch 'develop'
            }
            steps {
                echo 'Deploying to staging...'
                // Deployment steps
            }
        }

        stage('Deploy to Production') {
            when {
                branch 'main'
            }
            steps {
                input message: 'Deploy to production?', ok: 'Deploy'
                echo 'Deploying to production...'
                // Deployment steps
            }
        }
    }

    post {
        always {
            cleanWs()
        }
        failure {
            slackSend(
                color: 'danger',
                message: "Build failed: ${env.JOB_NAME} ${env.BUILD_NUMBER}"
            )
        }
        success {
            slackSend(
                color: 'good',
                message: "Build succeeded: ${env.JOB_NAME} ${env.BUILD_NUMBER}"
            )
        }
    }
}
```
