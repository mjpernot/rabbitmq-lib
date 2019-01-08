#!/usr/bin/python
# Classification (U)

"""Program:  test_rabbitmqpub_setup_queue.py

    Description:  Does unit testing on RabbitMQPub.setup_queue in
        rabbitmq_class.py program.

    Usage:
        test/unit/rabbitmq_class/test_rabbitmqpub_setup_queue.py

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


def rabbitmqpub_setup_queue(cfg):

    """Function:  rabbitmqpub_setup_queue

    Description:  Test setup_queue method in RabbitMQPub class.

    Arguments:
        (input) cfg -> RabbitMQ configuration module handler.

    """

    RQ = rabbitmq_class.RabbitMQPub(cfg.user, cfg.passwd, cfg.host, cfg.port,
                                    cfg.exchange_name, cfg.exchange_type,
                                    cfg.queue_name, cfg.routing_key,
                                    cfg.x_durable, cfg.q_durable,
                                    cfg.auto_delete)

    if isinstance(RQ, rabbitmq_class.RabbitMQPub):
        connect_status, err_msg = RQ.connect()

        if isinstance(RQ.connection,
                      pika.adapters.blocking_connection.BlockingConnection) \
                and RQ.connection._impl.connection_state > 0 \
                and connect_status:

            RQ.open_channel()

            if RQ.channel.is_open:
                RQ.setup_queue()

                try:
                    RQ.channel.exchange_declare(exchange=RQ.exchange,
                                                passive=True)

                    try:
                        RQ.channel.queue_declare(queue=RQ.queue_name,
                                                 passive=True)
                        print("\tPASS")

                    except pika.exceptions.ChannelClosed:
                        print("\tFAILURE:  Queue not found")

                except pika.exceptions.ChannelClosed:
                    print("\tWarning:  Exchange not found")

            else:
                print("\tFailed at is_open")
                print("\tChannel: %s" % RQ.channel)

        else:
            print("\tFailed at connection isinstance")
            print("\tConnection: %s" % RQ.connection)
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

    print("\nRabbitMQPub.setup_queue method testing...")
    rabbitmqpub_setup_queue(cfg)


if __name__ == "__main__":
    sys.exit(main())
