#!/usr/bin/python
# Classification (U)

"""Program:  rabbitmqcon_cleanup.py

    Description:  Cleanup the test exchange and queues.

    Usage:
        test/unit/rabbitmq_class/rabbitmqcon_cleanup.py

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


def rabbitmqcon_cleanup(cfg):

    """Function:  rabbitmqcon_cleanup

    Description:  Cleanup the test exchanges and queues.

    Arguments:
        (input) cfg -> RabbitMQ configuration module handler.

    """

    RQ = rabbitmq_class.RabbitMQCon(cfg.user, cfg.passwd, cfg.host, cfg.port,
                                    cfg.exchange_name, cfg.exchange_type,
                                    cfg.queue_name, cfg.routing_key,
                                    cfg.x_durable, cfg.q_durable,
                                    cfg.auto_delete)

    if isinstance(RQ, rabbitmq_class.RabbitMQCon):
        connect_status, err_msg = RQ.connect()

        if isinstance(RQ.connection,
                      pika.adapters.blocking_connection.BlockingConnection) \
                and RQ.connection._impl.connection_state > 0 \
                and connect_status:

            RQ.open_channel()

            if RQ.channel.is_open:
                RQ.setup_exchange()

                try:
                    RQ.channel.exchange_declare(exchange=RQ.exchange,
                                                passive=True)
                    RQ.create_queue()

                    try:
                        RQ.channel.queue_declare(queue=RQ.queue_name,
                                                 passive=True)
                        RQ.clear_queue()
                        RQ.drop_queue()
                        RQ.drop_exchange()
                        RQ.close_channel()

                        if RQ.channel.is_closed:

                            if connect_status \
                                    and RQ.connection._impl.connection_state \
                                    > 0:

                                RQ.close()

                                if RQ.connection._impl.connection_state == 0:
                                    print("\tEverything cleaned up")

                                else:
                                    print("\tFailed to close connection")
                                    print("\tConnection: %s" % RQ.connection)
                                    print("\tConnection State: %s" %
                                          RQ.connection._impl.connection_state)

                            else:
                                print("\tConnection not opened")

                        else:
                            print("\tFailure:  Channel did not close")
                            print("\tChannel: %s" % RQ.channel)

                    except pika.exceptions.ChannelClosed as msg:
                        print("\tWarning:  Unable to locate queue")
                        print("Error Msg: %s" % msg)

                except pika.exceptions.ChannelClosed as msg:
                    print("\tWarning:  Unable to find an exchange")
                    print("Error Msg: %s" % msg)

            else:
                print("\tFailure:  Unable to open channel")
                print("\tChannel: %s" % RQ.channel)

        else:
            print("\tFailure:  Unable to open connection")
            print("\tConnection: %s" % RQ.connection)
            print("\tError Msg: %s" % err_msg)

    else:
        print("\tFailure:  Unable to initialize")
        print("\tClass: %s" % rabbitmq_class.RabbitMQCon)


def main():

    """Function:  main

    Description:  Control the cleanup of exchanges and queues.

    Variables:
        None

    Arguments:
        None

    """

    cfg = load_module("rabbitmq", "test/unit/rabbitmq_class/config")

    print("\nRabbitMQCon cleanup...")
    rabbitmqcon_cleanup(cfg)


if __name__ == "__main__":
    sys.exit(main())
