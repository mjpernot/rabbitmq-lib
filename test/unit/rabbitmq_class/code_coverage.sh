#!/bin/bash
# Unit test code coverage for rabbitmq_class.py module.
# This will run the Python code coverage module against all unit test modules.
# This will show the amount of code that was tested and which lines of code
#	that was skipped during the test.

coverage erase

echo ""
echo "Running unit test modules in conjunction with coverage"
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/RabbitMQ_init.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/RabbitMQ_connect.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/RabbitMQ_close.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/RabbitMQPub_init.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/RabbitMQPub_bindqueue.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/RabbitMQPub_checkconfirm.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/rabbitmqpub_cleanup.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/RabbitMQPub_clearqueue.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/RabbitMQPub_closechannel.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/RabbitMQPub_createconnection.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/RabbitMQPub_createqueue.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/RabbitMQPub_dropconnection.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/RabbitMQPub_dropexchange.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/RabbitMQPub_dropqueue.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/RabbitMQPub_openchannel.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/RabbitMQPub_publishmsg.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/RabbitMQPub_setqueue.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/RabbitMQPub_setupexchange.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/RabbitMQPub_unbindqueue.py

echo ""
echo "Producing code coverage report"
coverage combine
coverage report -m
 
