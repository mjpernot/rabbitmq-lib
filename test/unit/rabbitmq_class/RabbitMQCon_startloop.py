#!/usr/bin/python
# Classification (U)

"""Program:  RabbitMQCon_startloop.py

    Description:  Unit testing of RabbitMQCon.start_loop in rabbitmq_class.py.

    Usage:
        test/unit/rabbitmq_class/RabbitMQCon_startloop.py

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


class StartLoop2(object):

    """Class:  StartLoop2

    Description:  Class stub holder for pika class.

    Methods:
        start_consuming -> start_consuming method.
        stop_consuming -> stop_consuming method.

    """

    def start_consuming(self):

        """Function:  start_consuming

        Description:  Stub holder for start_consuming function.

        Arguments:

        """

        raise KeyboardInterrupt

    def stop_consuming(self):

        """Function:  stop_consuming

        Description:  Stub holder for stop_consuming function.

        Arguments:

        """

        return True


class StartLoop(object):

    """Class:  StartLoop

    Description:  Class stub holder for pika class.

    Methods:
        start_consuming -> Stub holder for start_consuming function.

    """

    def start_consuming(self):

        """Function:  start_consuming

        Description:  Stub holder for start_consuming function.

        Arguments:

        """

        return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_raise_exception -> Test with raising exception.
        test_success_consume -> Test with successful consuming.

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

    @mock.patch("rabbitmq_class.RabbitMQCon.close")
    @mock.patch("rabbitmq_class.pika")
    def test_raise_exception(self, mock_pika, mock_close):

        """Function:  test_raise_exception

        Description:  Test with raising exception.

        Arguments:

        """

        mock_pika.PlainCredentials.return_value = "PlainCredentials"
        mock_pika.ConnectionParameters.return_value = "ConnectionParameters"
        mock_pika.BlockingConnection.return_value = "GoodConnection"
        mock_close.return_value = True
        rmq = rabbitmq_class.RabbitMQCon(self.name, "xxxxx", self.host,
                                         self.port)
        rmq.channel = StartLoop2()

        self.assertFalse(rmq.start_loop())

    @mock.patch("rabbitmq_class.RabbitMQCon.close")
    @mock.patch("rabbitmq_class.pika")
    def test_success_consume(self, mock_pika, mock_close):

        """Function:  test_success_consume

        Description:  Test with successful consuming.

        Arguments:

        """

        mock_pika.PlainCredentials.return_value = "PlainCredentials"
        mock_pika.ConnectionParameters.return_value = "ConnectionParameters"
        mock_pika.BlockingConnection.return_value = "GoodConnection"
        mock_close.return_value = True
        rmq = rabbitmq_class.RabbitMQCon(self.name, "xxxxx", self.host,
                                         self.port)
        rmq.channel = StartLoop()

        self.assertFalse(rmq.start_loop())


if __name__ == "__main__":
    unittest.main()
