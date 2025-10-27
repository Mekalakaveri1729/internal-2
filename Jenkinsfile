pipeline{
    agent any
    stages{
        stage("Run test selenium testcases"){
        steps{
            bat 'python -m pip install -r requirements.txt'
            bat 'start /B python app.py'
            bat 'ping 127.0.0.1 -n 5 > nul'
            bat 'python -m pytest-v'

    }
        }
    stage("build image"){
        steps{
            bat 'docker build -t testdemo:v1 .'
        }
    }
    stage("Docker login"){
        steps{
            bat 'docker login -u shivaji108 -p Kaveri@1729'
        }
    }
    stage("push image"){
        steps{
            bat 'docker tag testdemo:v1 shivaji108/testdemo:testimg'
            bat 'docker push shivaji108/testdemo:testimg'
        }
    }
    stage("deploy to kubernetes"){
        steps{
            bat 'kubectl apply -f deployment.yaml --validate=false'
            bat 'kubectl apply -f service.yaml'
        }
}
 }
 post{
    success{
        echo 'Pipeline completed successfully!'
    }
    failure{
        echo 'Pipeline failed. Please check the logs.'
    }
 }
}