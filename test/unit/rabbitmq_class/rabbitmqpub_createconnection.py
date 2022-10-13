# Classification (U)

"""Program:  rabbitmqpub_createconnection.py

    Description:  Unit test of rabbitmqpub.create_connection in
        rabbitmq_class.py.

    Usage:
        test/unit/rabbitmq_class/rabbitmqpub_createconnection.py

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


class CreateConnection(object):

    """Class:  CreateConnection

    Description:  Class stub holder for pika class.

    Methods:
        __init__
        exchange_declare

    """

    def __init__(self):

        """Function:  __init__

        Description:  Stub holder for __init__ function.

        Arguments:

        """

        self.is_open = True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_channel_is_closed
        test_channel_is_open
        test_fail_connect

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

    @mock.patch("rabbitmq_class.RabbitMQPub.open_channel")
    @mock.patch("rabbitmq_class.RabbitMQPub.connect")
    @mock.patch("rabbitmq_class.pika")
    def test_channel_is_closed(self, mock_pika, mock_connect, mock_channel):

        """Function:  test_channel_is_closed

        Description:  Test with channel is closed.

        Arguments:

        """

        mock_pika.PlainCredentials.return_value = "PlainCredentials"
        mock_pika.ConnectionParameters.return_value = "ConnectionParameters"
        mock_connect.return_value = (True, None)
        mock_channel.return_value = True
        rmq = rabbitmq_class.RabbitMQPub(self.name, "xxxxx")
        rmq.channel = CreateConnection()
        rmq.channel.is_open = False

        self.assertEqual(rmq.create_connection(),
                         (False, "Error:  Unable to open channel."))

    @mock.patch("rabbitmq_class.RabbitMQPub.setup_queue")
    @mock.patch("rabbitmq_class.RabbitMQPub.open_channel")
    @mock.patch("rabbitmq_class.RabbitMQPub.connect")
    @mock.patch("rabbitmq_class.pika")
    def test_channel_is_open(self, mock_pika, mock_connect, mock_channel,
                             mock_setup):

        """Function:  test_channel_is_open

        Description:  Test with channel is open.

        Arguments:

        """

        mock_pika.PlainCredentials.return_value = "PlainCredentials"
        mock_pika.ConnectionParameters.return_value = "ConnectionParameters"
        mock_connect.return_value = (True, None)
        mock_channel.return_value = True
        mock_setup.return_value = True
        rmq = rabbitmq_class.RabbitMQPub(self.name, "xxxxx")
        rmq.channel = CreateConnection()

        self.assertEqual(rmq.create_connection(), (True, None))

    @mock.patch("rabbitmq_class.RabbitMQPub.connect")
    @mock.patch("rabbitmq_class.pika")
    def test_fail_connect(self, mock_pika, mock_connect):

        """Function:  test_fail_connect

        Description:  Test with failure to connect.

        Arguments:

        """

        mock_pika.PlainCredentials.return_value = "PlainCredentials"
        mock_pika.ConnectionParameters.return_value = "ConnectionParameters"
        mock_connect.return_value = (False, "Failed to connect")
        rmq = rabbitmq_class.RabbitMQPub(self.name, "xxxxx")

        self.assertEqual(rmq.create_connection(), (False, "Failed to connect"))


if __name__ == "__main__":
    unittest.main()
