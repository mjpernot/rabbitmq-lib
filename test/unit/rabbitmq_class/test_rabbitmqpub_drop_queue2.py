#!/usr/bin/python
# Classification (U)

"""Program:  test_rabbitmqpub_drop_queue2.py

    Description:  Does unit testing on RabbitMQPub.drop_queue in
        rabbitmq_class.py program.

    Usage:
        test/unit/rabbitmq_class/test_rabbitmqpub_drop_queue2.py

    Arguments:
        None

"""

# Libraries and Global Variables

# Standard
import os
import sys

# Third-party
import pika

# Local
sys.path.append(os.getcwd())
import rabbitmq_class
import version

# Version
__version__ = version.__version__


def load_module(mod_name, mod_path):

    """Function:  load_module

    Description:  Load a Python module dynamically.

    Arguments:
        (input) mod_name -> Name of the module to load.
        (input) mod_path -> Directory path to the module to load.
        (output) Returns the module handler.

    """

    sys.path.append(mod_path)
    return __import__(mod_name)


def rabbitmqpub_drop_queue2(cfg):

    """Function:  rabbitmqpub_drop_queue2

    Description:  Test drop_queue method (with if_empty = False) in RabbitMQPub
        class.

    Arguments:
        (input) cfg -> RabbitMQ configuration module handler.

    """

    RQ = rabbitmq_class.RabbitMQPub(cfg.user, cfg.passwd, cfg.host, cfg.port,
                                    cfg.exchange_name, cfg.exchange_type,
                                    cfg.queue_name, cfg.routing_key,
                                    cfg.x_durable, cfg.q_durable,
                                    cfg.auto_delete)

    if isinstance(RQ, rabbitmq_class.RabbitMQPub):
        connect_status, err_msg = RQ.create_connection()

        if RQ.channel.is_open and connect_status:

            if RQ.publish_msg("Test message"):
                RQ.drop_queue(if_empty=False)
                print("\tPASS")

            else:
                print("\tFailed at publish message")
                print("\tConnection: %s" % RQ.connection)
                print("\tChannel: %s" % RQ.channel)

        else:
            print("\tFailed at is_open and connect_status")
            print("\tConnection: %s" % RQ.connection)
            print("\tChannel: %s" % RQ.channel)
            print("\tError: %s" % err_msg)

    else:
        print("\tFailed at class isinstance")
        print("\tClass: %s" % rabbitmq_class.RabbitMQPub)


def main():

    """Function:  main

    Description:  Control the testing of classes and methods.

    Variables:
        None

    Arguments:
        None

    """

    cfg = load_module("rabbitmq", "test/unit/rabbitmq_class/config")

    print("\nRabbitMQPub.drop_queue2 (with if_empty = False) testing...")
    rabbitmqpub_drop_queue2(cfg)


if __name__ == "__main__":
    sys.exit(main())
