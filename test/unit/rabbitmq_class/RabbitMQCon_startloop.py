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


class StartLoop2(object):

    """Class:  StartLoop2

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

        raise KeyboardInterrupt

    def stop_consuming(self):

        """Function:  stop_consuming

        Description:  Stub holder for stop_consuming function.

        Arguments:
            None

        """

        return True


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
        test_raise_exception -> Test with raising exception.
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

    @mock.patch("rabbitmq_class.RabbitMQCon.close")
    @mock.patch("rabbitmq_class.pika")
    def test_raise_exception(self, mock_pika, mock_close):

        """Function:  test_raise_exception

        Description:  Test with raising exception.

        Arguments:
            None

        """

        mock_pika.PlainCredentials.return_value = "PlainCredentials"
        mock_pika.ConnectionParameters.return_value = "ConnectionParameters"
        mock_pika.BlockingConnection.return_value = "GoodConnection"
        mock_close.return_value = True
        rq = rabbitmq_class.RabbitMQCon(self.name, "pwd", self.host, self.port)
        rq.channel = StartLoop2()

        self.assertFalse(rq.start_loop())

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
