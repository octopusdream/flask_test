pipeline {
    agent any
    environment{
        NEXUS_CREDS = credentials('nexus')
	JENKINS_IP = 3.37.129.159
    }
    stages {
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
                //sh 'docker push raj80dockerid/jenkinstest' (this will use the tag latest)    
                sh 'docker push ${JENKINS_IP}:5001/flask_test:$BUILD_NUMBER'
            }
        }
    }
    post {
        always {
            sh 'docker logout ${Jenkins_IP}:5001'
        }
    }
}
