# Declarative Pipeline (Jenkinsfile)

## Declarative Pipeline (Jenkinsfile)

```groovy
pipeline {
    agent { label 'linux-docker' }
    environment {
        REGISTRY = 'docker.io'
        IMAGE_NAME = 'myapp'
    }
    parameters {
        string(name: 'DEPLOY_ENV', defaultValue: 'staging')
    }
    stages {
        stage('Checkout') { steps { checkout scm } }
        stage('Install') { steps { sh 'npm ci' } }
        stage('Lint') { steps { sh 'npm run lint' } }
        stage('Test') {
            steps {
                sh 'npm run test:coverage'
                junit 'test-results.xml'
            }
        }
        stage('Build') {
            steps {
                sh 'npm run build'
                archiveArtifacts artifacts: 'dist/**/*'
            }
        }
        stage('Deploy') {
            when { branch 'main' }
            steps {
                sh 'kubectl set image deployment/app app=${REGISTRY}/${IMAGE_NAME}:latest'
            }
        }
    }
    post {
        always { cleanWs() }
        failure { echo 'Pipeline failed!' }
    }
}
```
