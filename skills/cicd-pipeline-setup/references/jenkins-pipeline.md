# Jenkins Pipeline

## Jenkins Pipeline

```groovy
// Jenkinsfile
pipeline {
    agent any

    options {
        buildDiscarder(logRotator(numToKeepStr: '10'))
        timeout(time: 1, unit: 'HOURS')
        timestamps()
    }

    environment {
        REGISTRY = 'gcr.io'
        PROJECT_ID = 'my-project'
        IMAGE_NAME = 'myapp'
        IMAGE_TAG = "${BUILD_NUMBER}-${GIT_COMMIT.take(7)}"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
                script {
                    GIT_COMMIT_MSG = sh(
                        script: "git log -1 --pretty=%B",
                        returnStdout: true
                    ).trim()
                }
            }
        }

        stage('Install') {
            steps {
                sh 'npm ci'
            }
        }

        stage('Lint') {
            steps {
                sh 'npm run lint'
            }
        }

        stage('Test') {
            steps {
                sh 'npm run test:coverage'
                publishHTML([
                    reportDir: 'coverage',
                    reportFiles: 'index.html',
                    reportName: 'Coverage Report'
                ])
            }
        }

        stage('Build Image') {
            when {
                branch 'main'
            }
            steps {
                script {
                    sh '''
                        docker build -t ${REGISTRY}/${PROJECT_ID}/${IMAGE_NAME}:${IMAGE_TAG} .
                        docker tag ${REGISTRY}/${PROJECT_ID}/${IMAGE_NAME}:${IMAGE_TAG} \
                                   ${REGISTRY}/${PROJECT_ID}/${IMAGE_NAME}:latest
                    '''
                }
            }
        }

        stage('Push Image') {
            when {
                branch 'main'
            }
            steps {
                sh '''
                    docker push ${REGISTRY}/${PROJECT_ID}/${IMAGE_NAME}:${IMAGE_TAG}
                    docker push ${REGISTRY}/${PROJECT_ID}/${IMAGE_NAME}:latest
                '''
            }
        }

        stage('Deploy Staging') {
            when {
                branch 'develop'
            }
            steps {
                sh '''
                    kubectl set image deployment/myapp myapp=${REGISTRY}/${PROJECT_ID}/${IMAGE_NAME}:${IMAGE_TAG} \
                        -n staging --record
                    kubectl rollout status deployment/myapp -n staging
                '''
            }
        }

        stage('Deploy Production') {
            when {
                branch 'main'
            }
            input {
                message "Deploy to production?"
                ok "Deploy"
            }
            steps {
                sh '''
                    kubectl set image deployment/myapp myapp=${REGISTRY}/${PROJECT_ID}/${IMAGE_NAME}:${IMAGE_TAG} \
                        -n production --record
                    kubectl rollout status deployment/myapp -n production
                '''
            }
        }
    }

    post {
        always {
            cleanWs()
        }
        success {
            slackSend(
                channel: '#deployments',
                message: "Build ${BUILD_NUMBER} succeeded on ${BRANCH_NAME}"
            )
        }
        failure {
            slackSend(
                channel: '#deployments',
                message: "Build ${BUILD_NUMBER} failed on ${BRANCH_NAME}"
            )
        }
    }
}
```
