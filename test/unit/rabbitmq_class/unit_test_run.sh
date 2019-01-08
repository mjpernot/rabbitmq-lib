#!/bin/bash
# Unit testing program for the RabbitMQ class methods.
# This will run all the units tests for this class.
# Will need to run this from the base directory where the class file 
#   is located at.

test/unit/rabbitmq_class/test_rabbitmq_init.py
test/unit/rabbitmq_class/test_rabbitmq_connect.py
test/unit/rabbitmq_class/test_rabbitmq_close.py

# Unit testing program for the RabbitMQPub class methods.

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

# Unit testing program for the RabbitMQCon class methods.

test/unit/rabbitmq_class/test_rabbitmqcon_init.py
test/unit/rabbitmq_class/test_rabbitmqcon_consume.py
test/unit/rabbitmq_class/test_rabbitmqcon_start_loop.py
test/unit/rabbitmq_class/test_rabbitmqcon_ack.py
test/unit/rabbitmq_class/rabbitmqcon_cleanup.py
