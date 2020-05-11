pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
        stage('Test') {
            steps {
                sh """
                virtualenv test_env
                source test_env/bin/activate
                pip2 install mock==2.0.0 --user
                pip2 install pika==0.11.0 --user
                ./test/unit/rabbitmq_class/create_rmqcon.py
                ./test/unit/rabbitmq_class/create_rmqpub.py
                ./test/unit/rabbitmq_class/pub_2_rmq.py
                ./test/unit/rabbitmq_class/RabbitMQ_init.py
                ./test/unit/rabbitmq_class/RabbitMQ_connect.py
                ./test/unit/rabbitmq_class/RabbitMQ_close.py
                ./test/unit/rabbitmq_class/RabbitMQPub_init.py
                ./test/unit/rabbitmq_class/RabbitMQPub_bindqueue.py
                ./test/unit/rabbitmq_class/RabbitMQPub_checkconfirm.py
                ./test/unit/rabbitmq_class/RabbitMQPub_clearqueue.py
                ./test/unit/rabbitmq_class/RabbitMQPub_closechannel.py
                ./test/unit/rabbitmq_class/RabbitMQPub_createconnection.py
                ./test/unit/rabbitmq_class/RabbitMQPub_createqueue.py
                ./test/unit/rabbitmq_class/RabbitMQPub_dropconnection.py
                ./test/unit/rabbitmq_class/RabbitMQPub_dropexchange.py
                ./test/unit/rabbitmq_class/RabbitMQPub_dropqueue.py
                ./test/unit/rabbitmq_class/RabbitMQPub_openchannel.py
                ./test/unit/rabbitmq_class/RabbitMQPub_publishmsg.py
                ./test/unit/rabbitmq_class/RabbitMQPub_setqueue.py
                ./test/unit/rabbitmq_class/RabbitMQPub_setupexchange.py
                ./test/unit/rabbitmq_class/RabbitMQPub_unbindqueue.py
                ./test/unit/rabbitmq_class/RabbitMQCon_init.py
                ./test/unit/rabbitmq_class/RabbitMQCon_consume.py
                ./test/unit/rabbitmq_class/RabbitMQCon_ack.py
                ./test/unit/rabbitmq_class/RabbitMQCon_startloop.py
                deactivate
                rm -rf test_env
                """
            }
        }
        stage('SonarQube analysis') {
            steps {
                sh './test/unit/sonarqube_code_coverage.sh'
                script {
                    scannerHome = tool 'sonar-scanner';
                }
                withSonarQubeEnv('Sonar') {
                    sh "${scannerHome}/bin/sonar-scanner -Dproject.settings=sonar-project.JACIDM.properties"
                }
            
            }
        }
        stage('Artifactory upload') {
            steps {
                script {
                    server = Artifactory.server('Artifactory')
                    server.credentialsId = 'svc-highpoint-artifactory'
                    uploadSpec = """{
                        "files": [
                            {
                                "pattern": "./*.py",
                                "recursive": false,
                                "excludePatterns": [],
                                "target": "pypi-proj-local/highpoint/rabbitmq-lib/"
                            },
                            {
                                "pattern": "./*.txt",
                                "recursive": false,
                                "excludePatterns": [],
                                "target": "pypi-proj-local/highpoint/rabbitmq-lib/"
                            },
                            {
                                "pattern": "./*.md",
                                "recursive": false,
                                "excludePatterns": [],
                                "target": "pypi-proj-local/highpoint/rabbitmq-lib/"
                            },
                            {
                                "pattern": "*.TEMPLATE",
                                "recursive": true,
                                "excludePatterns": [],
                                "target": "pypi-proj-local/highpoint/rabbitmq-lib/config/"
                            }
                        ]
                    }"""
                    server.upload(uploadSpec)
                }
            }
        }
    }
}
