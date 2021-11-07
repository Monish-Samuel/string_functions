pipeline {
    agent any

    stages {        
        stage('Compiling Stage'){
            steps{
                sh 'python3 string_calculator/main_methods.py'
            }
        }
        stage('Testing Stage'){
            steps{
                sh 'python3 string_calculator/test_main_methods.py'
            }
        }
        stage('Docker Image Build'){
            steps{
                sh 'docker build -t string_calculator .'
            }
        }
//         stage('Prep Stage'){
//             steps{
//                 powershell 'docker ps -q | % { docker stop $_ }'
//             }
//         }
        stage('Start Application'){
            steps{
                script{
                    sh 'docker run -d -p 8096:5000 --rm --name mypythonContainer string_calculator:latest'
                }
            }
        }
    }
}
