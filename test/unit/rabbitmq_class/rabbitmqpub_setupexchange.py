#!/usr/bin/python
# Classification (U)

"""Program:  rabbitmqpub_setupexchange.py

    Description:  Unit test of rabbitmqpub.setup_exchange in rabbitmq_class.py.

    Usage:
        test/unit/rabbitmq_class/rabbitmqpub_setupexchange.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os

if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest

# Third-party
import mock

# Local
sys.path.append(os.getcwd())
import rabbitmq_class
import version

__version__ = version.__version__


class SetupExchange(object):

    """Class:  SetupExchange

    Description:  Class stub holder for pika class.

    Methods:
        __init__ -> Class initialization.
        exchange_declare -> Stub holder for exchange_declare function.

    """

    def __init__(self):

        """Function:  __init__

        Description:  Stub holder for __init__ function.

        Arguments:

        """

        self.exchange = None
        self.exchange_type = None
        self.durable = None

    def exchange_declare(self, exchange, exchange_type, durable):

        """Function:  exchange_declare

        Description:  Stub holder for exchange_declare function.

        Arguments:
            exchange -> Arg stub holder.
            exchange_type -> Arg stub holder.
            durable -> Arg stub holder.

        """

        self.exchange = exchange
        self.exchange_type = exchange_type
        self.durable = durable

        return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_setup_exchange -> Test setup_exchange method.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.name = None
        self.host = "ServerName"
        self.port = 5555
        self.connection = None
        self.exchange_name = "Exchange_Name"
        self.queue_name = "Queue_Name"
        self.routing_key = "Route_Key"
        self.auto_delete = True

    @mock.patch("rabbitmq_class.pika")
    def test_setup_exchange(self, mock_pika):

        """Function:  test_setup_exchange

        Description:  Test setup_exchange method.

        Arguments:

        """

        mock_pika.PlainCredentials.return_value = "PlainCredentials"
        mock_pika.ConnectionParameters.return_value = "ConnectionParameters"
        rmq = rabbitmq_class.RabbitMQPub(self.name, "xxxxx")
        rmq.channel = SetupExchange()

        self.assertFalse(rmq.setup_exchange())


if __name__ == "__main__":
    unittest.main()
