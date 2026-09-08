// Pipeline alternativa em Jenkins, equivalente ao workflow do GitHub Actions.
// Pode ser usada caso a equipe opte por um Jenkins local/self-hosted.
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Baixando o código-fonte do repositório...'
                checkout scm
            }
        }

        stage('Instalar dependências') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Lint') {
            steps {
                sh 'flake8 app/ tests/ --max-line-length=100'
            }
        }

        stage('Testes automatizados') {
            steps {
                sh 'pytest tests/ -v'
            }
        }

        stage('Build da imagem Docker') {
            steps {
                sh 'docker build -t codefactory/task-manager-api:${BUILD_NUMBER} .'
            }
        }
    }

    post {
        success {
            echo 'Pipeline concluída com sucesso!'
        }
        failure {
            echo 'Pipeline falhou. Verifique os logs acima.'
        }
    }
}
