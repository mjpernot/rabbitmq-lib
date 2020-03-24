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
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/RabbitMQ_init.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/RabbitMQ_connect.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/RabbitMQ_close.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/RabbitMQPub_init.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/RabbitMQPub_bindqueue.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/RabbitMQPub_checkconfirm.py
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
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/RabbitMQCon_init.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/RabbitMQCon_consume.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/RabbitMQCon_ack.py
coverage run -a --source=rabbitmq_class test/unit/rabbitmq_class/RabbitMQCon_startloop.py

echo ""
echo "Producing code coverage report"
coverage combine
coverage report -m
coverage xml -i

