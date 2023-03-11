pipeline {
    agent any
    tools {
        python 'python3'
    }
    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[url: 'https://github.com/AnishDubey27/sky-guardian']]])
            }
        }
        stage('Build') {
            steps {
                sh 'docker-compose build'
            }
        }
        stage('Run Unit Tests') {
            steps {
                sh 'docker-compose run --rm web python manage.py test'
            }
        }
        stage('Deploy') {
            environment {
                DO_TOKEN = credentials('digitalocean-api-token')
            }
            steps {
                sh 'doctl auth init -t $DO_TOKEN'
                sh 'doctl apps create'
            }
        }
    }
}

