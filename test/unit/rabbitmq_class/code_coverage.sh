#!/bin/bash
# Unit test code coverage for rabbitmq_class.py module.
# This will run the Python code coverage module against all unit test modules.
# This will show the amount of code that was tested and which lines of code
#	that was skipped during the test.

coverage erase

echo ""
echo "Running unit test modules in conjunction with coverage"
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/test_rabbitmq_init.py 
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/test_rabbitmq_connect.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/test_rabbitmq_close.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/test_rabbitmqpub_bind_queue.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/test_rabbitmqpub_check_confirm.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/test_rabbitmqpub_clear_queue.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/test_rabbitmqpub_close.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/test_rabbitmqpub_close_channel.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/test_rabbitmqpub_connect.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/test_rabbitmqpub_create_connection.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/test_rabbitmqpub_create_queue.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/test_rabbitmqpub_drop_connection.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/test_rabbitmqpub_drop_exchange.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/test_rabbitmqpub_drop_exchange2.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/test_rabbitmqpub_drop_queue.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/test_rabbitmqpub_drop_queue2.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/test_rabbitmqpub_init.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/test_rabbitmqpub_open_channel.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/test_rabbitmqpub_publish_msg.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/test_rabbitmqpub_setup_exchange.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/test_rabbitmqpub_setup_queue.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/test_rabbitmqpub_unbind_queue.py
test/unit/rabbitmq_class/rabbitmqpub_cleanup.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/test_rabbitmqcon_ack.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/test_rabbitmqcon_consume.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/test_rabbitmqcon_init.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/test_rabbitmqcon_start_loop.py
test/unit/rabbitmq_class/rabbitmqcon_cleanup.py

echo ""
echo "Producing code coverage report"
coverage combine
coverage report -m
 
