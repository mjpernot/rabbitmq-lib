#!/usr/bin/python
# Classification (U)

"""Program:  test_rabbitmqcon_init.py

    Description:  Unit testing on RabbitMQCon.__init__ method in
        rabbitmq_class.py.

    Usage:
        test/unit/rabbitmq_class/test_rabbitmqcon_init.py

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


def rabbitmqcon_init(cfg):

    """Function:  rabbitmqcon_init

    Description:  Test __init__ method in RabbitMQCon class.

    Arguments:
        (input) cfg -> RabbitMQ configuration module handler.

    """

    RQ = rabbitmq_class.RabbitMQCon(cfg.user, cfg.passwd, cfg.host, cfg.port,
                                    cfg.exchange_name, cfg.exchange_type,
                                    cfg.queue_name, cfg.routing_key,
                                    cfg.x_durable, cfg.q_durable,
                                    cfg.auto_delete, cfg.no_ack)

    if isinstance(RQ, rabbitmq_class.RabbitMQCon):
        print("\tPASS")

    else:
        print("\tFAILURE")
        print("\tClass:  %s" % rabbitmq_class.RabbitMQCon)


def main():

    """Function:  main

    Description:  Control the testing of classes and methods.

    Variables:
        None

    Arguments:
        None

    """

    cfg = load_module("rabbitmq", "test/unit/rabbitmq_class/config")

    print("\nRabbitMQCon.__init__ method unit testing...")
    rabbitmqcon_init(cfg)


if __name__ == "__main__":
    sys.exit(main())
