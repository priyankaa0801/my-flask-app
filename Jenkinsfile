pipeline{
    agent any
    stages('Build'){
        steps{
            sh 'docker build -t registration-app'
        }
    }
    stage('Run')
    steps{
        sh 'docker rm -f Registration || true'
        sh 'docker run -d -p 5000:5000 --name registration registration-app'
    }
}
