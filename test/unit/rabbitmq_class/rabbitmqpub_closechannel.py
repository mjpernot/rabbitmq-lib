#!/usr/bin/python
# Classification (U)

"""Program:  rabbitmqpub_closechannel.py

    Description:  Unit test of rabbitmqpub.close_channel in rabbitmq_class.py.

    Usage:
        test/unit/rabbitmq_class/rabbitmqpub_closechannel.py

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


class CloseChannel(object):

    """Class:  CloseChannel

    Description:  Class stub holder for pika class.

    Methods:
        close

    """

    def close(self):

        """Function:  close

        Description:  Stub holder for close function.

        Arguments:

        """

        return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_close_channel

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
    def test_close_channel(self, mock_pika):

        """Function:  test_close_channel

        Description:  Test close_channel method.

        Arguments:

        """

        mock_pika.PlainCredentials.return_value = "PlainCredentials"
        mock_pika.ConnectionParameters.return_value = "ConnectionParameters"
        rmq = rabbitmq_class.RabbitMQPub(self.name, "xxxxx")
        rmq.channel = CloseChannel()

        self.assertFalse(rmq.close_channel())


if __name__ == "__main__":
    unittest.main()
