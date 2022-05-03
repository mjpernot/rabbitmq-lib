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
                pip2 install pika==1.2.0 --user
                ./test/unit/rabbitmq_class/create_rmqcon.py
                ./test/unit/rabbitmq_class/create_rmqpub.py
                ./test/unit/rabbitmq_class/pub_2_rmq.py
                ./test/unit/rabbitmq_class/rabbitmq_init.py
                ./test/unit/rabbitmq_class/rabbitmq_connect.py
                ./test/unit/rabbitmq_class/rabbitmq_close.py
                ./test/unit/rabbitmq_class/rabbitmqpub_init.py
                ./test/unit/rabbitmq_class/rabbitmqpub_bindqueue.py
                ./test/unit/rabbitmq_class/rabbitmqpub_checkconfirm.py
                ./test/unit/rabbitmq_class/rabbitmqpub_clearqueue.py
                ./test/unit/rabbitmq_class/rabbitmqpub_closechannel.py
                ./test/unit/rabbitmq_class/rabbitmqpub_createconnection.py
                ./test/unit/rabbitmq_class/rabbitmqpub_createqueue.py
                ./test/unit/rabbitmq_class/rabbitmqpub_dropconnection.py
                ./test/unit/rabbitmq_class/rabbitmqpub_dropexchange.py
                ./test/unit/rabbitmq_class/rabbitmqpub_dropqueue.py
                ./test/unit/rabbitmq_class/rabbitmqpub_openchannel.py
                ./test/unit/rabbitmq_class/rabbitmqpub_publishmsg.py
                ./test/unit/rabbitmq_class/rabbitmqpub_setqueue.py
                ./test/unit/rabbitmq_class/rabbitmqpub_setupexchange.py
                ./test/unit/rabbitmq_class/rabbitmqpub_unbindqueue.py
                ./test/unit/rabbitmq_class/rabbitmqcon_init.py
                ./test/unit/rabbitmq_class/rabbitmqcon_consume.py
                ./test/unit/rabbitmq_class/rabbitmqcon_ack.py
                ./test/unit/rabbitmq_class/rabbitmqcon_startloop.py
                ./test/unit/rabbitmq_class/rabbitmqbase_api_delete.py
                ./test/unit/rabbitmq_class/rabbitmqbase_api_get.py
                ./test/unit/rabbitmq_class/rabbitmqbase_api_post.py
                ./test/unit/rabbitmq_class/rabbitmqbase_api_put.py
                ./test/unit/rabbitmq_class/rabbitmqbase_delete.py
                ./test/unit/rabbitmq_class/rabbitmqbase_get.py
                ./test/unit/rabbitmq_class/rabbitmqbase_init.py
                ./test/unit/rabbitmq_class/rabbitmqbase_post.py
                ./test/unit/rabbitmq_class/rabbitmqbase_put.py
                ./test/unit/rabbitmq_class/rabbitmqadmin_create_exchange_for_vhost.py
                ./test/unit/rabbitmq_class/rabbitmqadmin_create_vhost.py
                ./test/unit/rabbitmq_class/rabbitmqadmin_delete_connection.py
                ./test/unit/rabbitmq_class/rabbitmqadmin_delete_vhost.py
                ./test/unit/rabbitmq_class/rabbitmqadmin_get_channel.py
                ./test/unit/rabbitmq_class/rabbitmqadmin_get_cluster_name.py
                ./test/unit/rabbitmq_class/rabbitmqadmin_get_connection.py
                ./test/unit/rabbitmq_class/rabbitmqadmin_get_definitions.py
                ./test/unit/rabbitmq_class/rabbitmqadmin_get_exchange_for_vhost.py
                ./test/unit/rabbitmq_class/rabbitmqadmin_get_node.py
                ./test/unit/rabbitmq_class/rabbitmqadmin_list_bindings.py
                ./test/unit/rabbitmq_class/rabbitmqadmin_list_bindings_for_vhost.py
                ./test/unit/rabbitmq_class/rabbitmqadmin_list_channels.py
                ./test/unit/rabbitmq_class/rabbitmqadmin_list_connections.py
                ./test/unit/rabbitmq_class/rabbitmqadmin_list_connection_channels.py
                ./test/unit/rabbitmq_class/rabbitmqadmin_list_consumers.py
                ./test/unit/rabbitmq_class/rabbitmqadmin_list_consumers_for_vhost.py
                ./test/unit/rabbitmq_class/rabbitmqadmin_list_exchanges.py
                ./test/unit/rabbitmq_class/rabbitmqadmin_list_exchanges_for_vhost.py
                ./test/unit/rabbitmq_class/rabbitmqadmin_list_extensions.py
                ./test/unit/rabbitmq_class/rabbitmqadmin_list_nodes.py
                ./test/unit/rabbitmq_class/rabbitmqadmin_list_users.py
                ./test/unit/rabbitmq_class/rabbitmqadmin_list_vhosts.py
                ./test/unit/rabbitmq_class/rabbitmqadmin_overview.py
                ./test/unit/rabbitmq_class/rabbitmqadmin_post_definitions.py
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
                    server.credentialsId = 'art-svc-highpoint-dev'
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
    post {
        always {
            cleanWs disableDeferredWipeout: true
        }
    }
}
