#!/usr/bin/python
# Classification (U)

"""Program:  test_rabbitmqcon_ack.py

    Description:  Unit testing on RabbitMQCon.ack method in rabbitmq_class.py.

    Usage:
        test/unit/rabbitmq_class/test_rabbitmqcon_ack.py

    Arguments:
        None

"""

# Libraries and Global Variables

# Standard
import os
import sys

# Third-party

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


def rabbitmqpub_publish_msg(cfg, msg):

    """Function:  rabbitmqpub_publish_msg

    Description:  Publish test message for testing RabbitMQCon class.

    Arguments:
        (input) cfg -> RabbitMQ configuration module handler.
        (input) msg -> Body of test message.

    """

    RP = rabbitmq_class.RabbitMQPub(cfg.user, cfg.passwd, cfg.host, cfg.port,
                                    cfg.exchange_name, cfg.exchange_type,
                                    cfg.queue_name, cfg.routing_key,
                                    cfg.x_durable, cfg.q_durable,
                                    cfg.auto_delete)

    if isinstance(RP, rabbitmq_class.RabbitMQPub):

        connect_status, err_msg = RP.create_connection()

        if RP.channel.is_open and connect_status:

            if RP.publish_msg(msg):

                RP.drop_connection()

                if not RP.channel.is_closed:
                    print("\tFailed at first is_closed")
                    print("\tConnection: %s" % RP.connection)
                    print("\tChannel: %s" % RP.channel)

            else:
                print("\tFailed at publish_msg")
                print("\tConnection: %s" % RP.connection)
                print("\tChannel: %s" % RP.channel)

        else:
            print("\tFailed at is_open and connect_status")
            print("\tConnection: %s" % RP.connection)
            print("\tChannel: %s" % RP.channel)
            print("\tError: %s" % err_msg)

    else:
        print("\tFailed at first isinstance")
        print("\tClass: %s" % rabbitmq_class.RabbitMQPub)


def rabbitmqcon_ack(cfg, msg):

    """Function:  rabbitmqcon_ack

    Description:  Test ack method in RabbitMQCon class.

    Arguments:
        (input) cfg -> RabbitMQ configuration module handler.
        (input) msg -> Body of test message.

    """

    def callback(channel, method, properties, body):

        """Function:  callback

        Description:  Call back function for the consume method.

        Arguments:
            (input) channel -> Information on RabbitMQ channel.
            (input) method -> Information on RabbitMQ method.
            (input) properties -> Properties on RabbitMQ channel.
            (input) body -> Message body from RabbitMQ queue.

        """

        if msg == body:
            print("\tPASS")

        else:
            print("\tFAILURE")
            print("\tMessage Sent:  %s" % msg)
            print("\tMessage Rcvd:  %s" % body)

        RQ.ack(method.delivery_tag)
        RQ.drop_connection()

    connect_status = None

    RQ = rabbitmq_class.RabbitMQCon(cfg.user, cfg.passwd, cfg.host, cfg.port,
                                    cfg.exchange_name, cfg.exchange_type,
                                    cfg.queue_name, cfg.routing_key,
                                    cfg.x_durable, cfg.q_durable,
                                    cfg.auto_delete, cfg.no_ack)

    if isinstance(RQ, rabbitmq_class.RabbitMQCon):
        connect_status, err_msg = RQ.create_connection()

        if connect_status and RQ.channel.is_open:
            tag_name = RQ.consume(callback)

            if tag_name.startswith("ctag"):
                RQ.start_loop()

                if not RQ.channel.is_closed:
                    print("\tFailed at second is_closed")
                    print("\tConnection: %s" % RQ.connection)
                    print("\tChannel: %s" % RQ.channel)

            else:
                print("\tFailed at tag_name")
                print("\tTag: %s" % tag_name)

        else:
            print("\tFailed to connnect to RabbitMQ Node...")
            print("\tMessage:  %s" % err_msg)

    else:
        print("\tFailed at second isinstance")
        print("\tClass: %s" % rabbitmq_class.RabbitMQCon)


def main():

    """Function:  main

    Description:  Control the testing of classes and methods.

    Variables:
        None

    Arguments:
        None

    """

    cfg = load_module("rabbitmq", "test/unit/rabbitmq_class/config")
    msg = "Test message"

    print("\nRabbitMQCon.ack method unit testing...")
    rabbitmqpub_publish_msg(cfg, msg)
    rabbitmqcon_ack(cfg, msg)


if __name__ == "__main__":
    sys.exit(main())
