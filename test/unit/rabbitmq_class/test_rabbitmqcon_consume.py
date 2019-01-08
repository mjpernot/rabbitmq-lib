#!/usr/bin/python
# Classification (U)

"""Program:  test_rabbitmqcon_consume.py

    Description:  Unit testing on RabbitMQCon.consume method in
        rabbitmq_class.py.

    Usage:
        test/unit/rabbitmq_class/test_rabbitmqcon_consume.py

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


def rabbitmqcon_consume(cfg):

    """Function:  rabbitmqcon_consume

    Description:  Test consume method in RabbitMQCon class.

    Arguments:
        (input) cfg -> RabbitMQ configuration module handler.

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

        print("Body: %r" % body)
        RQ.ack(method.delivery_tag)

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
                print("\tPASS")

            else:
                print("\tFAILURE")
                print("Tag: %s" % (tag_name))

        else:
            print("Failed to connnect to RabbuitMQ Node...")
            print("Message:  %s" % (err_msg))

    else:
        print("\tFailed at isinstance")
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

    print("\nRabbitMQCon.consume method unit testing...")
    rabbitmqcon_consume(cfg)


if __name__ == "__main__":
    sys.exit(main())
