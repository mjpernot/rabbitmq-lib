# Classification (U)

"""Program:  rabbitmqpub_dropconnection.py

    Description:  Unit test of rabbitmqpub.drop_connection in
        rabbitmq_class.py.

    Usage:
        test/unit/rabbitmq_class/rabbitmqpub_dropconnection.py

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


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_drop_connection

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

    @mock.patch("rabbitmq_class.RabbitMQPub.close_channel")
    @mock.patch("rabbitmq_class.RabbitMQPub.close")
    @mock.patch("rabbitmq_class.pika")
    def test_drop_connection(self, mock_pika, mock_close, mock_channel):

        """Function:  test_drop_connection

        Description:  Test drop_connection method.

        Arguments:

        """

        mock_pika.PlainCredentials.return_value = "PlainCredentials"
        mock_pika.ConnectionParameters.return_value = "ConnectionParameters"
        mock_close.return_value = True
        mock_channel.return_value = True
        rmq = rabbitmq_class.RabbitMQPub(self.name, "xxxxx")

        self.assertFalse(rmq.drop_connection())


if __name__ == "__main__":
    unittest.main()
