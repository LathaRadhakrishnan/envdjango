pipeline {
agent any

environment {
    
    AWS_DEFAULT_REGION    = 'us-west-1'
    APPLICATION_NAME      = 'test2'
    ENVIRONMENT_NAME      = 'Test2-env'
    
    
}  

stages {
    stage ('GIT Checkout'){
        steps {
            git changelog: false, poll: false,branch: 'main',url: 'https://github.com/LathaRadhakrishnan/envdjango.git'
        }
    }
    
    stage('build') {
      steps {
         sh 'pip install -r requirements.txt'
    }
}

    stage('Unit Test'){
      steps{
        sh 'python3 manage.py test latha.tests.HelloWorldViewTest '
    }
}
stage('Integration Test'){
    steps{
        sh 'python3 manage.py test latha.tests.HelloWorldIntegrationTest'
    }
}

stage('Run static code analysis') {
            steps {
                script {
                    // Run pylint on the Django project in the root directory
                    sh 'pylint latha'
                }
            }
    }


 stage('Package') {
            steps {
                // Package your Django application
                sh 'zip -r application.zip .'
            }
        }
          
        
        
 stage('Deploy to Elastic Beanstalk') {
            steps {
                script {
                    // Deploy the application to Elastic Beanstalk
                    withAWS(credentials: 'aws-credentials', region: AWS_DEFAULT_REGION) {
                        sh "eb init -p python ${APPLICATION_NAME} --region ${AWS_DEFAULT_REGION}"
                        sh "eb use ${ENVIRONMENT_NAME}"
                        sh "eb deploy --staged --region ${AWS_DEFAULT_REGION}"
                    }
                }
            }
        }
        

stage("Pen Testing"){
    steps{
        script{
            
            def sudoPassword = 'Alpha@23'
           
            sh "echo '${sudoPassword}' | sudo -S docker run -t ghcr.io/zaproxy/zaproxy:stable zap-full-scan.py -t http://test2-env.eba-mmwpscnj.us-west-1.elasticbeanstalk.com/helloworld/hello/ "
        }
    }
}
    
}
}