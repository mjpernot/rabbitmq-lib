#!/bin/bash
# Unit test code coverage for rabbitmq_class.py module.
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

echo ""
echo "Producing code coverage report"
coverage combine
coverage report -m
 
