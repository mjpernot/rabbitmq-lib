#!/bin/bash
# Unit testing program for the RabbitMQCon class methods.
# This will run all the units tests for this class.
# Will need to run this from the base directory where the class file 
#   is located at.

test/unit/rabbitmq_class/test_rabbitmqcon_init.py
test/unit/rabbitmq_class/test_rabbitmqcon_consume.py
test/unit/rabbitmq_class/test_rabbitmqcon_start_loop.py
test/unit/rabbitmq_class/test_rabbitmqcon_ack.py
test/unit/rabbitmq_class/rabbitmqcon_cleanup.py
