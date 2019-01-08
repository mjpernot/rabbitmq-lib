#!/bin/bash
# Unit testing program for the RabbitMQPub class methods.
# This will run all the units tests for this class.
# Will need to run this from the base directory where the class file 
#   is located at.

test/unit/rabbitmq_class/test_rabbitmqpub_init.py
test/unit/rabbitmq_class/test_rabbitmqpub_connect.py
test/unit/rabbitmq_class/test_rabbitmqpub_open_channel.py
test/unit/rabbitmq_class/test_rabbitmqpub_setup_exchange.py
test/unit/rabbitmq_class/test_rabbitmqpub_create_queue.py
test/unit/rabbitmq_class/test_rabbitmqpub_bind_queue.py
test/unit/rabbitmq_class/test_rabbitmqpub_check_confirm.py
test/unit/rabbitmq_class/test_rabbitmqpub_unbind_queue.py
test/unit/rabbitmq_class/test_rabbitmqpub_drop_queue.py
test/unit/rabbitmq_class/test_rabbitmqpub_drop_exchange.py
test/unit/rabbitmq_class/test_rabbitmqpub_close_channel.py
test/unit/rabbitmq_class/test_rabbitmqpub_close.py
test/unit/rabbitmq_class/test_rabbitmqpub_create_connection.py
test/unit/rabbitmq_class/test_rabbitmqpub_drop_connection.py
test/unit/rabbitmq_class/test_rabbitmqpub_publish_msg.py
test/unit/rabbitmq_class/test_rabbitmqpub_clear_queue.py
test/unit/rabbitmq_class/test_rabbitmqpub_setup_queue.py
test/unit/rabbitmq_class/test_rabbitmqpub_drop_queue2.py
test/unit/rabbitmq_class/test_rabbitmqpub_drop_exchange2.py
test/unit/rabbitmq_class/rabbitmqpub_cleanup.py
