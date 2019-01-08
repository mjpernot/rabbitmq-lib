#!/usr/bin/python
# Classification (U)

"""Program:  test_rabbitmq_connect.py

    Description:  Does unit testing on RabbitMQ.connect method in
        rabbitmq_class.py.

    Usage:
        test/unit/rabbitmq_class/test_rabbitmq_connect.py

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


def rabbitmq_connect(cfg):

    """Function:  rabbitmq_connect

    Description:  Test connect method in RabbitMQ class.

    Arguments:
        (input) cfg -> RabbitMQ configuration module handler.

    """

    RQ = rabbitmq_class.RabbitMQ(cfg.user, cfg.passwd, cfg.host, cfg.port)

    if isinstance(RQ, rabbitmq_class.RabbitMQ):
        connect_status, err_msg = RQ.connect()

        if isinstance(RQ.connection,
                      pika.adapters.blocking_connection.BlockingConnection) \
                and RQ.connection._impl.connection_state > 0 \
                and connect_status:

            print("\tPASS")

        else:
            print("\tFAILURE")
            print("\tConnection: %s" % RQ.connection)
            print("\tError: %s" % err_msg)

    else:
        print("\tFailed at class isinstance")
        print("\tClass: %s" % rabbitmq_class.RabbitMQ)


def main():

    """Function:  main

    Description:  Control the testing of classes and methods.

    Variables:
        None

    Arguments:
        None

    """

    cfg = load_module("rabbitmq", "test/unit/rabbitmq_class/config")

    print("\nRabbitMQ.connect method testing...")
    rabbitmq_connect(cfg)


if __name__ == "__main__":
    sys.exit(main())
