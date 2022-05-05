#!/bin/bash
# Unit test code coverage for SonarQube to cover all library modules in rabitmq-lib.
# This will run the Python code coverage module against all unit test modules.
# This will show the amount of code that was tested and which lines of code
#	that was skipped during the test.

coverage erase

echo ""
echo "Running unit test modules in conjunction with coverage"
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/create_rmqcon.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/create_rmqpub.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/pub_2_rmq.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/rabbitmq_init.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/rabbitmq_connect.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/rabbitmq_close.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/rabbitmqpub_init.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/rabbitmqpub_bindqueue.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/rabbitmqpub_checkconfirm.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/rabbitmqpub_clearqueue.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/rabbitmqpub_closechannel.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/rabbitmqpub_createconnection.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/rabbitmqpub_createqueue.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/rabbitmqpub_dropconnection.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/rabbitmqpub_dropexchange.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/rabbitmqpub_dropqueue.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/rabbitmqpub_openchannel.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/rabbitmqpub_publishmsg.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/rabbitmqpub_setqueue.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/rabbitmqpub_setupexchange.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/rabbitmqpub_unbindqueue.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/rabbitmqcon_init.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/rabbitmqcon_consume.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/rabbitmqcon_ack.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/rabbitmqcon_startloop.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/rabbitmqbase_api_delete.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/rabbitmqbase_api_get.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/rabbitmqbase_api_post.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/rabbitmqbase_api_put.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/rabbitmqbase_delete.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/rabbitmqbase_get.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/rabbitmqbase_init.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/rabbitmqbase_post.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/rabbitmqbase_put.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/rabbitmqadmin_create_exchange_for_vhost.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/rabbitmqadmin_create_policy_for_vhost.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/rabbitmqadmin_create_queue_for_vhost.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/rabbitmqadmin_create_topic_permission.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/rabbitmqadmin_create_user.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/rabbitmqadmin_create_user_permission.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/rabbitmqadmin_create_vhost.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/rabbitmqadmin_delete_connection.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/rabbitmqadmin_delete_policy_for_vhost.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/rabbitmqadmin_delete_topic_permission.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/rabbitmqadmin_delete_user.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/rabbitmqadmin_delete_user_permission.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/rabbitmqadmin_delete_vhost.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/rabbitmqadmin_get_channel.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/rabbitmqadmin_get_cluster_name.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/rabbitmqadmin_get_connection.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/rabbitmqadmin_get_definitions.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/rabbitmqadmin_get_exchange_for_vhost.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/rabbitmqadmin_get_node.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/rabbitmqadmin_get_policy_for_vhost.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/rabbitmqadmin_get_queue_for_vhost.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/rabbitmqadmin_get_user.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/rabbitmqadmin_get_vhost.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/rabbitmqadmin_get_vhost_user_perms.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/rabbitmqadmin_is_vhost_alive.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/rabbitmqadmin_list_bindings.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/rabbitmqadmin_list_bindings_for_vhost.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/rabbitmqadmin_list_channels.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/rabbitmqadmin_list_connections.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/rabbitmqadmin_list_connection_channels.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/rabbitmqadmin_list_consumers.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/rabbitmqadmin_list_consumers.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/rabbitmqadmin_list_consumers_for_vhost.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/rabbitmqadmin_list_exchanges.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/rabbitmqadmin_list_exchanges_for_vhost.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/rabbitmqadmin_list_extensions.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/rabbitmqadmin_list_nodes.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/rabbitmqadmin_list_permissions.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/rabbitmqadmin_list_policies.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/rabbitmqadmin_list_policies_for_vhost.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/rabbitmqadmin_list_topic_permissions.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/rabbitmqadmin_list_users.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/rabbitmqadmin_list_user_permissions.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/rabbitmqadmin_list_user_topic_permissions.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/rabbitmqadmin_list_vhosts.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/rabbitmqadmin_list_vhost_topic_permissions.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/rabbitmqadmin_list_vhost_user_topic_perms.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/rabbitmqadmin_overview.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/rabbitmqadmin_post_definitions.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/rabbitmqadmin_whoami.py

echo ""
echo "Producing code coverage report"
coverage combine
coverage report -m
coverage xml -i

