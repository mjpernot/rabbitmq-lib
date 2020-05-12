#!/usr/bin/python
# Classification (U)

"""Program:  RabbitMQPub_dropexchange.py

    Description:  Unit test of RabbitMQPub.drop_exchange in rabbitmq_class.py.

    Usage:
        test/unit/rabbitmq_class/RabbitMQPub_dropexchange.py

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


class DropExchange(object):

    """Class:  DropExchange

    Description:  Class stub holder for pika class.

    Methods:
        __init__ -> Class initialization.
        queue_unbind -> Stub holder for queue_unbind function.

    """

    def __init__(self):

        """Function:  __init__

        Description:  Stub holder for __init__ function.

        Arguments:

        """

        self.exchange = None
        self.if_unused = None

    def exchange_delete(self, exchange, if_unused):

        """Function:  exchange_delete

        Description:  Stub holder for queue_unbind function.

        Arguments:
            exchange -> Arg stub holder.
            if_unused -> Arg stub holder.

        """

        self.exchange = exchange
        self.if_unused = if_unused

        return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_drop_exchange -> Test drop_exchange method.

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
        self.body = "Message_Body"

    @mock.patch("rabbitmq_class.pika")
    def test_drop_exchange(self, mock_pika):

        """Function:  test_drop_exchange

        Description:  Test drop_exchange method.

        Arguments:

        """

        mock_pika.PlainCredentials.return_value = "PlainCredentials"
        mock_pika.ConnectionParameters.return_value = "ConnectionParameters"
        mock_pika.BasicProperties.return_value = True
        rmq = rabbitmq_class.RabbitMQPub(self.name, "xxxxx")
        rmq.channel = DropExchange()

        self.assertFalse(rmq.drop_exchange())


if __name__ == "__main__":
    unittest.main()
