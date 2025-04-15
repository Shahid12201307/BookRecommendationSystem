pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/Shahid12201307/BookRecommendationSystem.git'
            }
        }
        stage('Install Requirements') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Application') {
            steps {
                sh 'python app/app.py'
            }
        }
    }
}
