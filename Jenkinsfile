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
                bat 'docker build -t string_calculator .'
            }
        }
        stage('Docker Hub image'){
            steps{
                powershell 'docker tag string_calculator:latest string_calculator:${BUILD_NUMBER}'
            }
        }
    }
}
