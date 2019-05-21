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


class pika(object):

    """Class:  FileOpen2

    Description:  Class stub holder for file open class.

    Super-Class:  None

    Sub-Classes:  None

    Methods:
        BlockingConnection -> Stub holder for BlockingConnection function.

    """

    def BlockingConnection(self):

        """Function:  BlockingConnection

        Description:  Stub holder for BlockingConnection function.

        Arguments:
            None

        """

        raise pika.exceptions.ConnectionClosed('ConnectionClosedMsg')


def pika_raise():

    """Function:  pika_raise

    Description:  Method stub holder for NNNNNN.

    Arguments:
        arg1 -> Stub holder for params argument.

    """

    raise pika.exceptions.ConnectionClosed('ConnectionClosedMsg')


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Super-Class:  unittest.TestCase

    Sub-Classes:  None

    Methods:
        setUp -> Initialize testing environment.
        test_success_connect -> Test with successful connection.
        test_fail_closed -> Test with failed connection - ConnectionClosed.

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
        self.open2 = pika()

    @unittest.skip("Not working")
    @mock.patch("rabbitmq_class.pika.BlockingConnection")
    @mock.patch("rabbitmq_class.pika.ConnectionParameters")
    @mock.patch("rabbitmq_class.pika.PlainCredentials")
    def test_fail_closed(self, mock_pika1, mock_pika2, mock_pika3):

        """Function:  test_fail_closed

        Description:  Test with failed connection - ConnectionClosed.

        Arguments:
            None

        """


        mock_pika1.return_value = "PlainCredentials"
        mock_pika2.return_value = "ConnectionParameters"
        mock_pika3.side_effect = [self.open2]
        rq = rabbitmq_class.RabbitMQ(self.name, "pwd", self.host, self.port)

        self.assertEqual(rq.connect(), (False, "ConnectionClosed"))

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
