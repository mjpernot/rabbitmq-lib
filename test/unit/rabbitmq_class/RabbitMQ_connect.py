#!/usr/bin/python
# Classification (U)

"""Program:  RabbitMQ_connect.py

    Description:  Unit testing of RabbitMQ.connect in rabbitmq_class.py.

    Usage:
        test/unit/rabbitmq_class/RabbitMQ_connect.py

    Arguments:
        None

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

    Super-Class:  unittest.TestCase

    Sub-Classes:  None

    Methods:
        setUp -> Initialize testing environment.
        test_fail_auth -> Test with failed authenication - AuthenticationError.
        test_fail_closed -> Test with failed connection - ConnectionClosed.
        test_success_connect -> Test with successful connection.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:
            None

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
            None

        """

        mock_creds.return_value = "PlainCredentials"
        mock_conn.return_value = "ConnectionParameters"
        mock_blk.side_effect = \
            pika.exceptions.AMQPConnectionError('GeneralError')
        rq = rabbitmq_class.RabbitMQ(self.name, "pwd", self.host, self.port)

        status, msg = rq.connect()
        self.assertEqual((status, str(msg)), (False, "GeneralError"))

    @mock.patch("rabbitmq_class.pika.BlockingConnection")
    @mock.patch("rabbitmq_class.pika.ConnectionParameters")
    @mock.patch("rabbitmq_class.pika.PlainCredentials")
    def test_fail_auth(self, mock_creds, mock_conn, mock_blk):

        """Function:  test_fail_auth

        Description:  Test with failed authenication - AuthenticationError.

        Arguments:
            None

        """

        mock_creds.return_value = "PlainCredentials"
        mock_conn.return_value = "ConnectionParameters"
        mock_blk.side_effect = \
            pika.exceptions.ProbableAuthenticationError('AuthenticationError')
        rq = rabbitmq_class.RabbitMQ(self.name, "pwd", self.host, self.port)

        status, msg = rq.connect()
        self.assertEqual((status, str(msg)), (False, "AuthenticationError"))

    @mock.patch("rabbitmq_class.pika.BlockingConnection")
    @mock.patch("rabbitmq_class.pika.ConnectionParameters")
    @mock.patch("rabbitmq_class.pika.PlainCredentials")
    def test_fail_closed(self, mock_creds, mock_conn, mock_blk):

        """Function:  test_fail_closed

        Description:  Test with failed connection - ConnectionClosed.

        Arguments:
            None

        """

        mock_creds.return_value = "PlainCredentials"
        mock_conn.return_value = "ConnectionParameters"
        mock_blk.side_effect = \
            pika.exceptions.ConnectionClosed(123, 'ConnectionClosedMsg')
        rq = rabbitmq_class.RabbitMQ(self.name, "pwd", self.host, self.port)

        status, msg = rq.connect()
        self.assertEqual((status, str(msg)),
                         (False, str((123, "ConnectionClosedMsg"))))

    @mock.patch("rabbitmq_class.pika")
    def test_success_connect(self, mock_pika):

        """Function:  test_success_connect

        Description:  Test with successful connection.

        Arguments:
            None

        """

        mock_pika.PlainCredentials.return_value = "PlainCredentials"
        mock_pika.ConnectionParameters.return_value = "ConnectionParameters"
        mock_pika.BlockingConnection.return_value = "GoodConnection"
        rq = rabbitmq_class.RabbitMQ(self.name, "pwd", self.host, self.port)

        self.assertEqual(rq.connect(), (True, None))


if __name__ == "__main__":
    unittest.main()
