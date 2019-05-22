#!/usr/bin/python
# Classification (U)

"""Program:  RabbitMQCon_startloop.py

    Description:  Unit testing of RabbitMQCon.start_loop in rabbitmq_class.py.

    Usage:
        test/unit/rabbitmq_class/RabbitMQCon_startloop.py

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


class StartLoop(object):

    """Class:  StartLoop

    Description:  Class stub holder for pika class.

    Super-Class:  None

    Sub-Classes:  None

    Methods:
        start_consuming -> Stub holder for start_consuming function.

    """

    def start_consuming(self):

        """Function:  start_consuming

        Description:  Stub holder for start_consuming function.

        Arguments:
            None

        """

        return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Super-Class:  unittest.TestCase

    Sub-Classes:  None

    Methods:
        setUp -> Initialize testing environment.
        test_success_consume -> Test with successful consuming.

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

    @unittest.skip("Not done")
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

    @unittest.skip("Not done")
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

    @unittest.skip("Not done")
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
            pika.exceptions.ConnectionClosed('ConnectionClosedMsg')
        rq = rabbitmq_class.RabbitMQ(self.name, "pwd", self.host, self.port)

        status, msg = rq.connect()
        self.assertEqual((status, str(msg)), (False, "ConnectionClosedMsg"))

    @mock.patch("rabbitmq_class.RabbitMQCon.close")
    @mock.patch("rabbitmq_class.pika")
    def test_success_consume(self, mock_pika, mock_close):

        """Function:  test_success_consume

        Description:  Test with successful consuming.

        Arguments:
            None

        """


        mock_pika.PlainCredentials.return_value = "PlainCredentials"
        mock_pika.ConnectionParameters.return_value = "ConnectionParameters"
        mock_pika.BlockingConnection.return_value = "GoodConnection"
        mock_close.return_value = True
        rq = rabbitmq_class.RabbitMQCon(self.name, "pwd", self.host, self.port)
        rq.channel = StartLoop()

        self.assertFalse(rq.start_loop())


if __name__ == "__main__":
    unittest.main()
