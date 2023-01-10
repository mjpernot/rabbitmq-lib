# Classification (U)

"""Program:  rabbitmqpub_openchannel.py

    Description:  Unit test of rabbitmqpub.open_channel in rabbitmq_class.py.

    Usage:
        test/unit/rabbitmq_class/rabbitmqpub_openchannel.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest
import mock

# Local
sys.path.append(os.getcwd())
import rabbitmq_class
import version

__version__ = version.__version__


class OpenChannel(object):

    """Class:  OpenChannel

    Description:  Class stub holder for pika class.

    Methods:
        close

    """

    def channel(self):

        """Function:  channel

        Description:  Stub holder for channel function.

        Arguments:

        """

        return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_open_channel

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
    def test_open_channel(self, mock_pika):

        """Function:  test_open_channel

        Description:  Test open_channel method.

        Arguments:

        """

        mock_pika.PlainCredentials.return_value = "PlainCredentials"
        mock_pika.ConnectionParameters.return_value = "ConnectionParameters"
        rmq = rabbitmq_class.RabbitMQPub(self.name, "xxxxx")
        rmq.connection = OpenChannel()
        rmq.open_channel()

        self.assertEqual(rmq.channel, True)


if __name__ == "__main__":
    unittest.main()
