pipeline {
    agent any
    environment{
        NEXUS_CREDS = credentials('nexus')
	JENKINS_IP = '3.37.129.159'
	SLACK_CHANNEL = '#jenkins'
    }
    stages {
	stage('Start') {
                steps {
                    slackSend (channel: SLACK_CHANNEL, color: '#FFFF00', message: "STARTED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]' (${env.BUILD_URL})")
                }
        }
        stage('Clone Repo') {
            steps {
                checkout scm
                sh 'ls *'
            }
        }
        stage('Build Image') {
            steps {
		sh '/etc/init.d/docker start'
		sh 'docker build -t ${JENKINS_IP}:5001/flask_test:$BUILD_NUMBER .'
            }
        }
        stage('Docker Login') {
            steps {
                sh 'echo $NEXUS_CREDS_PSW | docker login ${JENKINS_IP}:5001 -u $NEXUS_CREDS_USR --password-stdin'                
            }
        }
        stage('Docker Push') {
            steps {
                sh 'docker push ${JENKINS_IP}:5001/flask_test:$BUILD_NUMBER'
            }
        }
    }
    post {
        always {
            sh 'docker logout ${Jenkins_IP}:5001'
        }
	success {
            slackSend (channel: SLACK_CHANNEL, color: '#00FF00', message: "SUCCESSFUL: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]' (${env.BUILD_URL})")
        }
        failure {
            slackSend (channel: SLACK_CHANNEL, color: '#FF0000', message: "FAILED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]' (${env.BUILD_URL})")
        }
    }
}
