#!/bin/bash
# Unit testing program for the RabbitMQ class methods.
# This will run all the units tests for this class.
# Will need to run this from the base directory where the class file 
#   is located at.

test/unit/rabbitmq_class/create_rmqcon.py
test/unit/rabbitmq_class/create_rmqpub.py
test/unit/rabbitmq_class/RabbitMQ_init.py
test/unit/rabbitmq_class/RabbitMQ_connect.py
test/unit/rabbitmq_class/RabbitMQ_close.py
test/unit/rabbitmq_class/RabbitMQPub_init.py
test/unit/rabbitmq_class/RabbitMQPub_bindqueue.py
test/unit/rabbitmq_class/RabbitMQPub_checkconfirm.py
test/unit/rabbitmq_class/RabbitMQPub_clearqueue.py
test/unit/rabbitmq_class/RabbitMQPub_closechannel.py
test/unit/rabbitmq_class/RabbitMQPub_createconnection.py
test/unit/rabbitmq_class/RabbitMQPub_createqueue.py
test/unit/rabbitmq_class/RabbitMQPub_dropconnection.py
test/unit/rabbitmq_class/RabbitMQPub_dropexchange.py
test/unit/rabbitmq_class/RabbitMQPub_dropqueue.py
test/unit/rabbitmq_class/RabbitMQPub_openchannel.py
test/unit/rabbitmq_class/RabbitMQPub_publishmsg.py
test/unit/rabbitmq_class/RabbitMQPub_setqueue.py
test/unit/rabbitmq_class/RabbitMQPub_setupexchange.py
test/unit/rabbitmq_class/RabbitMQPub_unbindqueue.py
test/unit/rabbitmq_class/RabbitMQCon_init.py
test/unit/rabbitmq_class/RabbitMQCon_consume.py
test/unit/rabbitmq_class/RabbitMQCon_ack.py
test/unit/rabbitmq_class/RabbitMQCon_startloop.py

