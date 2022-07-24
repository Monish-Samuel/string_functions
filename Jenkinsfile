pipeline {
    agent any

    stages {        
        stage('Compiling Stage'){
            steps{
                bat 'python string_calculator/main_methods.py'
            }
        }
        stage('Testing Stage'){
            steps{
                bat 'python string_calculator/test_main_methods.py'
            }
        }
        stage('Docker Image Build'){
            steps{
                bat 'docker build --no-cache -t string_calculator .'
            }
        }
        stage('Start Application'){
            steps{
                bat 'docker ps -f name=mypythonContainer -q | xargs --no-run-if-empty docker container stop'
                bat 'docker container ls -a -fname=mypythonContainer -q | xargs -r docker container rm'
                script {
                    bat 'docker run -d -p 8096:5000 --rm --name mypythonContainer string_calculator:latest'
                }
            }
        }
    }
}
