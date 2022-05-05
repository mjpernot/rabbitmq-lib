#!/bin/bash
# Unit testing program for the RabbitMQ class methods.
# This will run all the units tests for this class.
# Will need to run this from the base directory where the class file 
#   is located at.

test/unit/rabbitmq_class/create_rmqcon.py
test/unit/rabbitmq_class/create_rmqpub.py
test/unit/rabbitmq_class/pub_2_rmq.py
test/unit/rabbitmq_class/rabbitmq_init.py
test/unit/rabbitmq_class/rabbitmq_connect.py
test/unit/rabbitmq_class/rabbitmq_close.py
test/unit/rabbitmq_class/rabbitmqpub_init.py
test/unit/rabbitmq_class/rabbitmqpub_bindqueue.py
test/unit/rabbitmq_class/rabbitmqpub_checkconfirm.py
test/unit/rabbitmq_class/rabbitmqpub_clearqueue.py
test/unit/rabbitmq_class/rabbitmqpub_closechannel.py
test/unit/rabbitmq_class/rabbitmqpub_createconnection.py
test/unit/rabbitmq_class/rabbitmqpub_createqueue.py
test/unit/rabbitmq_class/rabbitmqpub_dropconnection.py
test/unit/rabbitmq_class/rabbitmqpub_dropexchange.py
test/unit/rabbitmq_class/rabbitmqpub_dropqueue.py
test/unit/rabbitmq_class/rabbitmqpub_openchannel.py
test/unit/rabbitmq_class/rabbitmqpub_publishmsg.py
test/unit/rabbitmq_class/rabbitmqpub_setqueue.py
test/unit/rabbitmq_class/rabbitmqpub_setupexchange.py
test/unit/rabbitmq_class/rabbitmqpub_unbindqueue.py
test/unit/rabbitmq_class/rabbitmqcon_init.py
test/unit/rabbitmq_class/rabbitmqcon_consume.py
test/unit/rabbitmq_class/rabbitmqcon_ack.py
test/unit/rabbitmq_class/rabbitmqcon_startloop.py
test/unit/rabbitmq_class/rabbitmqbase_api_delete.py
test/unit/rabbitmq_class/rabbitmqbase_api_get.py
test/unit/rabbitmq_class/rabbitmqbase_api_post.py
test/unit/rabbitmq_class/rabbitmqbase_api_put.py
test/unit/rabbitmq_class/rabbitmqbase_delete.py
test/unit/rabbitmq_class/rabbitmqbase_get.py
test/unit/rabbitmq_class/rabbitmqbase_init.py
test/unit/rabbitmq_class/rabbitmqbase_post.py
test/unit/rabbitmq_class/rabbitmqbase_put.py
test/unit/rabbitmq_class/rabbitmqadmin_create_exchange_for_vhost.py
test/unit/rabbitmq_class/rabbitmqadmin_create_policy_for_vhost.py
test/unit/rabbitmq_class/rabbitmqadmin_create_queue_for_vhost.py
test/unit/rabbitmq_class/rabbitmqadmin_create_topic_permission.py
test/unit/rabbitmq_class/rabbitmqadmin_create_user.py
test/unit/rabbitmq_class/rabbitmqadmin_create_user_permission.py
test/unit/rabbitmq_class/rabbitmqadmin_create_vhost.py
test/unit/rabbitmq_class/rabbitmqadmin_delete_connection.py
test/unit/rabbitmq_class/rabbitmqadmin_delete_policy_for_vhost.py
test/unit/rabbitmq_class/rabbitmqadmin_delete_topic_permission.py
test/unit/rabbitmq_class/rabbitmqadmin_delete_user.py
test/unit/rabbitmq_class/rabbitmqadmin_delete_user_permission.py
test/unit/rabbitmq_class/rabbitmqadmin_delete_vhost.py
test/unit/rabbitmq_class/rabbitmqadmin_get_channel.py
test/unit/rabbitmq_class/rabbitmqadmin_get_cluster_name.py
test/unit/rabbitmq_class/rabbitmqadmin_get_connection.py
test/unit/rabbitmq_class/rabbitmqadmin_get_definitions.py
test/unit/rabbitmq_class/rabbitmqadmin_get_exchange_for_vhost.py
test/unit/rabbitmq_class/rabbitmqadmin_get_node.py
test/unit/rabbitmq_class/rabbitmqadmin_get_policy_for_vhost.py
test/unit/rabbitmq_class/rabbitmqadmin_get_queue_for_vhost.py
test/unit/rabbitmq_class/rabbitmqadmin_get_user.py
test/unit/rabbitmq_class/rabbitmqadmin_get_vhost.py
test/unit/rabbitmq_class/rabbitmqadmin_get_vhost_user_perms.py
test/unit/rabbitmq_class/rabbitmqadmin_is_vhost_alive.py
test/unit/rabbitmq_class/rabbitmqadmin_list_bindings.py
test/unit/rabbitmq_class/rabbitmqadmin_list_bindings_for_vhost.py
test/unit/rabbitmq_class/rabbitmqadmin_list_channels.py
test/unit/rabbitmq_class/rabbitmqadmin_list_connections.py
test/unit/rabbitmq_class/rabbitmqadmin_list_connection_channels.py
test/unit/rabbitmq_class/rabbitmqadmin_list_consumers.py
test/unit/rabbitmq_class/rabbitmqadmin_list_consumers_for_vhost.py
test/unit/rabbitmq_class/rabbitmqadmin_list_exchanges.py
test/unit/rabbitmq_class/rabbitmqadmin_list_exchanges_for_vhost.py
test/unit/rabbitmq_class/rabbitmqadmin_list_extensions.py
test/unit/rabbitmq_class/rabbitmqadmin_list_nodes.py
test/unit/rabbitmq_class/rabbitmqadmin_list_permissions.py
test/unit/rabbitmq_class/rabbitmqadmin_list_policies.py
test/unit/rabbitmq_class/rabbitmqadmin_list_policies_for_vhost.py
test/unit/rabbitmq_class/rabbitmqadmin_list_topic_permissions.py
test/unit/rabbitmq_class/rabbitmqadmin_list_users.py
test/unit/rabbitmq_class/rabbitmqadmin_list_user_permissions.py
test/unit/rabbitmq_class/rabbitmqadmin_list_user_topic_permissions.py
test/unit/rabbitmq_class/rabbitmqadmin_list_vhosts.py
test/unit/rabbitmq_class/rabbitmqadmin_list_vhost_topic_permissions.py
test/unit/rabbitmq_class/rabbitmqadmin_list_vhost_user_topic_perms.py
test/unit/rabbitmq_class/rabbitmqadmin_overview.py
test/unit/rabbitmq_class/rabbitmqadmin_post_definitions.py
test/unit/rabbitmq_class/rabbitmqadmin_whoami.py

