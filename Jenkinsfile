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
        stage('Prep Stage'){
            steps{
                powershell 'docker kill $(docker ps -q)'
                powershell 'docker rm $(docker ps -a -q)'
                powershell 'docker rmi $(docker images -q)'
            }
        }
        stage('Docker Image Build'){
            steps{
                bat 'docker build -t string_calculator .'
            }
        }
        stage('Start Application'){
            steps{
                powershell 'docker run -d -p 8096:5000 --rm --name mypythonContainer string_calculator:latest'
            }
        }
    }
}
