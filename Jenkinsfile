pipeline {
    agent any
    environment{
        NEXUS_CREDS = credentials('nexus')
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
                //sh 'docker build -t yusine51/jenkinstest ./pushdockerimage/' (this will use the tag latest)
	        sh 'docker build -t 3.37.129.51:5001/flask_test:$BUILD_NUMBER .'
            }
        }
        stage('Docker Login') {
            steps {
                //sh 'docker login -u $NEXUS_CREDS_USR -p $NEXUS_CREDS_PSW' (this will leave the password visible)
                sh 'echo $NEXUS_CREDS_PSW | docker login 3.37.129.51:5001 -u $NEXUS_CREDS_USR --password-stdin'                
            }
        }
        stage('Docker Push') {
            steps {
                //sh 'docker push raj80dockerid/jenkinstest' (this will use the tag latest)    
                sh 'docker push 3.37.129.51:5001/flask_test:$BUILD_NUMBER'
            }
        }
    }
    post {
        always {
            sh 'docker logout 3.37.129.51:5001'
        }
    }
}
