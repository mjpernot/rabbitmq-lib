# Classification (U)

"""Program:  rabbitmq_connect.py

    Description:  Unit testing of rabbitmq.connect in rabbitmq_class.py.

    Usage:
        test/unit/rabbitmq_class/rabbitmq_connect.py

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
import pika

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
        test_fail_auth
        test_fail_closed
        test_success_connect

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

    @mock.patch("rabbitmq_class.pika.BlockingConnection")
    @mock.patch("rabbitmq_class.pika.ConnectionParameters")
    @mock.patch("rabbitmq_class.pika.PlainCredentials")
    def test_fail_error(self, mock_creds, mock_conn, mock_blk):

        """Function:  test_fail_error

        Description:  Test with failed general error - GeneralError.

        Arguments:

        """

        mock_creds.return_value = "PlainCredentials"
        mock_conn.return_value = "ConnectionParameters"
        mock_blk.side_effect = \
            pika.exceptions.AMQPConnectionError('GeneralError')
        rmq = rabbitmq_class.RabbitMQ(self.name, "xxxxx", self.host, self.port)

        status, msg = rmq.connect()
        self.assertEqual((status, str(msg)), (False, "GeneralError"))

    @mock.patch("rabbitmq_class.pika.BlockingConnection")
    @mock.patch("rabbitmq_class.pika.ConnectionParameters")
    @mock.patch("rabbitmq_class.pika.PlainCredentials")
    def test_fail_auth(self, mock_creds, mock_conn, mock_blk):

        """Function:  test_fail_auth

        Description:  Test with failed authenication - AuthenticationError.

        Arguments:

        """

        mock_creds.return_value = "PlainCredentials"
        mock_conn.return_value = "ConnectionParameters"
        mock_blk.side_effect = \
            pika.exceptions.ProbableAuthenticationError('AuthenticationError')
        rmq = rabbitmq_class.RabbitMQ(self.name, "xxxxx", self.host, self.port)

        status, msg = rmq.connect()
        self.assertEqual((status, str(msg)), (False, "AuthenticationError"))

    @mock.patch("rabbitmq_class.pika.BlockingConnection")
    @mock.patch("rabbitmq_class.pika.ConnectionParameters")
    @mock.patch("rabbitmq_class.pika.PlainCredentials")
    def test_fail_closed(self, mock_creds, mock_conn, mock_blk):

        """Function:  test_fail_closed

        Description:  Test with failed connection - ConnectionClosed.

        Arguments:

        """

        mock_creds.return_value = "PlainCredentials"
        mock_conn.return_value = "ConnectionParameters"
        mock_blk.side_effect = \
            pika.exceptions.ConnectionClosed(123, 'ConnectionClosedMsg')
        rmq = rabbitmq_class.RabbitMQ(self.name, "xxxxx", self.host, self.port)

        status, msg = rmq.connect()
        self.assertEqual((status, str(msg)),
                         (False, str((123, "ConnectionClosedMsg"))))

    @mock.patch("rabbitmq_class.pika")
    def test_success_connect(self, mock_pika):

        """Function:  test_success_connect

        Description:  Test with successful connection.

        Arguments:

        """

        mock_pika.PlainCredentials.return_value = "PlainCredentials"
        mock_pika.ConnectionParameters.return_value = "ConnectionParameters"
        mock_pika.BlockingConnection.return_value = "GoodConnection"
        rmq = rabbitmq_class.RabbitMQ(self.name, "xxxxx", self.host, self.port)

        self.assertEqual(rmq.connect(), (True, None))


if __name__ == "__main__":
    unittest.main()
