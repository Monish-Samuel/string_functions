pipeline {
    agent any

    stages {        
        stage('Compiling Stage'){
            steps{
                sh 'python string_calculator/main_methods.py'
            }
        }
        stage('Testing Stage'){
            steps{
                sh 'python string_calculator/test_main_methods.py'
            }
        }
        stage('Docker Image Build'){
            steps{
                sh 'docker build -t string_calculator .'
            }
        }
        stage('Start Application'){
            steps{
                sh 'docker ps -f name=mypythonContainer -q | xargs --no-run-if-empty docker container stop'
                sh 'docker container ls -a -fname=mypythonContainer -q | xargs -r docker container rm'
                script {
                    sh 'docker run -d -p 8096:5000 --rm --name mypythonContainer string_calculator:latest'
                }
            }
        }
    }
}
