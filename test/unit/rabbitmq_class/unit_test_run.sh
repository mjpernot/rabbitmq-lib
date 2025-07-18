#!/bin/bash
# Unit testing program for the RabbitMQ class methods.
# This will run all the units tests for this class.
# Will need to run this from the base directory where the class file 
#   is located at.

/usr/bin/python ./test/unit/rabbitmq_class/create_rmqcon.py
/usr/bin/python ./test/unit/rabbitmq_class/create_rmqpub.py
/usr/bin/python ./test/unit/rabbitmq_class/pub_2_rmq.py
/usr/bin/python ./test/unit/rabbitmq_class/rabbitmq_init.py
/usr/bin/python ./test/unit/rabbitmq_class/rabbitmq_connect.py
/usr/bin/python ./test/unit/rabbitmq_class/rabbitmq_close.py
/usr/bin/python ./test/unit/rabbitmq_class/rabbitmqpub_init.py
/usr/bin/python ./test/unit/rabbitmq_class/rabbitmqpub_bindqueue.py
/usr/bin/python ./test/unit/rabbitmq_class/rabbitmqpub_checkconfirm.py
/usr/bin/python ./test/unit/rabbitmq_class/rabbitmqpub_clearqueue.py
/usr/bin/python ./test/unit/rabbitmq_class/rabbitmqpub_closechannel.py
/usr/bin/python ./test/unit/rabbitmq_class/rabbitmqpub_connect_queue.py
/usr/bin/python ./test/unit/rabbitmq_class/rabbitmqpub_createconnection.py
/usr/bin/python ./test/unit/rabbitmq_class/rabbitmqpub_createqueue.py
/usr/bin/python ./test/unit/rabbitmq_class/rabbitmqpub_dropconnection.py
/usr/bin/python ./test/unit/rabbitmq_class/rabbitmqpub_dropexchange.py
/usr/bin/python ./test/unit/rabbitmq_class/rabbitmqpub_dropqueue.py
/usr/bin/python ./test/unit/rabbitmq_class/rabbitmqpub_openchannel.py
/usr/bin/python ./test/unit/rabbitmq_class/rabbitmqpub_queue_count.py
/usr/bin/python ./test/unit/rabbitmq_class/rabbitmqpub_publishmsg.py
/usr/bin/python ./test/unit/rabbitmq_class/rabbitmqpub_setqueue.py
/usr/bin/python ./test/unit/rabbitmq_class/rabbitmqpub_setupexchange.py
/usr/bin/python ./test/unit/rabbitmq_class/rabbitmqpub_unbindqueue.py
/usr/bin/python ./test/unit/rabbitmq_class/rabbitmqcon_init.py
/usr/bin/python ./test/unit/rabbitmq_class/rabbitmqcon_consume.py
/usr/bin/python ./test/unit/rabbitmq_class/rabbitmqcon_ack.py
/usr/bin/python ./test/unit/rabbitmq_class/rabbitmqcon_startloop.py
/usr/bin/python ./test/unit/rabbitmq_class/rabbitmqbase_api_delete.py
/usr/bin/python ./test/unit/rabbitmq_class/rabbitmqbase_api_get.py
/usr/bin/python ./test/unit/rabbitmq_class/rabbitmqbase_api_post.py
/usr/bin/python ./test/unit/rabbitmq_class/rabbitmqbase_api_put.py
/usr/bin/python ./test/unit/rabbitmq_class/rabbitmqbase_delete.py
/usr/bin/python ./test/unit/rabbitmq_class/rabbitmqbase_get.py
/usr/bin/python ./test/unit/rabbitmq_class/rabbitmqbase_init.py
/usr/bin/python ./test/unit/rabbitmq_class/rabbitmqbase_post.py
/usr/bin/python ./test/unit/rabbitmq_class/rabbitmqbase_put.py
/usr/bin/python ./test/unit/rabbitmq_class/rabbitmqadmin_create_exchange_for_vhost.py
/usr/bin/python ./test/unit/rabbitmq_class/rabbitmqadmin_create_policy_for_vhost.py
/usr/bin/python ./test/unit/rabbitmq_class/rabbitmqadmin_create_queue_for_vhost.py
/usr/bin/python ./test/unit/rabbitmq_class/rabbitmqadmin_create_topic_permission.py
/usr/bin/python ./test/unit/rabbitmq_class/rabbitmqadmin_create_user.py
/usr/bin/python ./test/unit/rabbitmq_class/rabbitmqadmin_create_user_permission.py
/usr/bin/python ./test/unit/rabbitmq_class/rabbitmqadmin_create_vhost.py
/usr/bin/python ./test/unit/rabbitmq_class/rabbitmqadmin_delete_connection.py
/usr/bin/python ./test/unit/rabbitmq_class/rabbitmqadmin_delete_policy_for_vhost.py
/usr/bin/python ./test/unit/rabbitmq_class/rabbitmqadmin_delete_queue_for_vhost.py
/usr/bin/python ./test/unit/rabbitmq_class/rabbitmqadmin_delete_topic_permission.py
/usr/bin/python ./test/unit/rabbitmq_class/rabbitmqadmin_delete_user.py
/usr/bin/python ./test/unit/rabbitmq_class/rabbitmqadmin_delete_user_permission.py
/usr/bin/python ./test/unit/rabbitmq_class/rabbitmqadmin_delete_vhost.py
/usr/bin/python ./test/unit/rabbitmq_class/rabbitmqadmin_get_channel.py
/usr/bin/python ./test/unit/rabbitmq_class/rabbitmqadmin_get_cluster_name.py
/usr/bin/python ./test/unit/rabbitmq_class/rabbitmqadmin_get_connection.py
/usr/bin/python ./test/unit/rabbitmq_class/rabbitmqadmin_get_definitions.py
/usr/bin/python ./test/unit/rabbitmq_class/rabbitmqadmin_get_exchange_for_vhost.py
/usr/bin/python ./test/unit/rabbitmq_class/rabbitmqadmin_get_node.py
/usr/bin/python ./test/unit/rabbitmq_class/rabbitmqadmin_get_policy_for_vhost.py
/usr/bin/python ./test/unit/rabbitmq_class/rabbitmqadmin_get_queue_for_vhost.py
/usr/bin/python ./test/unit/rabbitmq_class/rabbitmqadmin_get_user.py
/usr/bin/python ./test/unit/rabbitmq_class/rabbitmqadmin_get_vhost.py
/usr/bin/python ./test/unit/rabbitmq_class/rabbitmqadmin_get_vhost_user_perms.py
/usr/bin/python ./test/unit/rabbitmq_class/rabbitmqadmin_is_vhost_alive.py
/usr/bin/python ./test/unit/rabbitmq_class/rabbitmqadmin_list_bindings.py
/usr/bin/python ./test/unit/rabbitmq_class/rabbitmqadmin_list_bindings_for_vhost.py
/usr/bin/python ./test/unit/rabbitmq_class/rabbitmqadmin_list_channels.py
/usr/bin/python ./test/unit/rabbitmq_class/rabbitmqadmin_list_connections.py
/usr/bin/python ./test/unit/rabbitmq_class/rabbitmqadmin_list_connection_channels.py
/usr/bin/python ./test/unit/rabbitmq_class/rabbitmqadmin_list_consumers.py
/usr/bin/python ./test/unit/rabbitmq_class/rabbitmqadmin_list_consumers_for_vhost.py
/usr/bin/python ./test/unit/rabbitmq_class/rabbitmqadmin_list_exchanges.py
/usr/bin/python ./test/unit/rabbitmq_class/rabbitmqadmin_list_exchanges_for_vhost.py
/usr/bin/python ./test/unit/rabbitmq_class/rabbitmqadmin_list_extensions.py
/usr/bin/python ./test/unit/rabbitmq_class/rabbitmqadmin_list_nodes.py
/usr/bin/python ./test/unit/rabbitmq_class/rabbitmqadmin_list_permissions.py
/usr/bin/python ./test/unit/rabbitmq_class/rabbitmqadmin_list_policies.py
/usr/bin/python ./test/unit/rabbitmq_class/rabbitmqadmin_list_policies_for_vhost.py
/usr/bin/python ./test/unit/rabbitmq_class/rabbitmqadmin_list_queues.py
/usr/bin/python ./test/unit/rabbitmq_class/rabbitmqadmin_list_queues_for_vhost.py
/usr/bin/python ./test/unit/rabbitmq_class/rabbitmqadmin_list_topic_permissions.py
/usr/bin/python ./test/unit/rabbitmq_class/rabbitmqadmin_list_users.py
/usr/bin/python ./test/unit/rabbitmq_class/rabbitmqadmin_list_user_permissions.py
/usr/bin/python ./test/unit/rabbitmq_class/rabbitmqadmin_list_user_topic_permissions.py
/usr/bin/python ./test/unit/rabbitmq_class/rabbitmqadmin_list_vhosts.py
/usr/bin/python ./test/unit/rabbitmq_class/rabbitmqadmin_list_vhost_topic_permissions.py
/usr/bin/python ./test/unit/rabbitmq_class/rabbitmqadmin_list_vhost_user_topic_perms.py
/usr/bin/python ./test/unit/rabbitmq_class/rabbitmqadmin_overview.py
/usr/bin/python ./test/unit/rabbitmq_class/rabbitmqadmin_post_definitions.py
/usr/bin/python ./test/unit/rabbitmq_class/rabbitmqadmin_whoami.py

