stages {
    stage('Clone Repo') {
        steps {
            git 'https://github.com/Shahid12201307/BookRecommendationSystem.git'
        }
    }

    stage('Install Dependencies') {
        steps {
            dir('Devops_project') {
                sh 'pip install -r requirements.txt'
            }
        }
    }

    stage('Build Docker Image') {
        steps {
            dir('Devops_project') {
                sh 'docker build -t book-mood-app .'
            }
        }
    }

    stage('Run Container (Test)') {
        steps {
            dir('Devops_project') {
                sh 'docker run -d -p 5000:5000 book-mood-app'
            }
        }
    }

    stage('Cleanup') {
        steps {
            sh 'docker stop $(docker ps -q --filter ancestor=book-mood-app) || true'
            sh 'docker rm $(docker ps -aq --filter ancestor=book-mood-app) || true'
        }
    }
}
