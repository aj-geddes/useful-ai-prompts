# Scripted Pipeline

## Scripted Pipeline (Groovy)

```groovy
// Jenkinsfile - Scripted Pipeline

node('linux-docker') {
    def imageTag = sh(returnStdout: true, script: 'git rev-parse --short HEAD').trim()
    def registry = 'docker.io'

    try {
        stage('Checkout') { checkout scm }
        stage('Install') { sh 'npm ci' }
        stage('Test') { sh 'npm test' }
        stage('Build') { sh 'npm run build' }

        currentBuild.result = 'SUCCESS'
    } catch (Exception e) {
        currentBuild.result = 'FAILURE'
        error("Build failed: ${e.message}")
    }
}
```


## Multi-Branch Pipeline

```groovy
pipeline {
    agent any
    stages {
        stage('Build') { steps { sh 'npm run build' } }
        stage('Test') { steps { sh 'npm test' } }
        stage('Deploy') {
            when { branch 'main' }
            steps { sh 'npm run deploy:prod' }
        }
    }
}
```


## Parameterized Pipeline

```groovy
pipeline {
    agent any
    parameters {
        string(name: 'VERSION', defaultValue: '1.0.0', description: 'Version to release')
        choice(name: 'ENV', choices: ['staging', 'prod'], description: 'Deployment environment')
    }
    stages {
        stage('Build') { steps { sh 'npm run build' } }
        stage('Test') { steps { sh 'npm test' } }
        stage('Deploy') {
            steps { sh "npm run deploy:${params.ENV}" }
        }
    }
}
```


## Pipeline with Credentials

```groovy
pipeline {
    agent any
    environment {
        DOCKER_CREDS = credentials('docker-hub')
    }
    stages {
        stage('Build & Push') {
            steps {
                sh '''
                    echo $DOCKER_CREDS_PSW | docker login -u $DOCKER_CREDS_USR --password-stdin
                    docker build -t myapp:latest .
                    docker push myapp:latest
                '''
            }
        }
    }
}
```
