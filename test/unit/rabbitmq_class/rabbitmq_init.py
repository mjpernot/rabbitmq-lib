#!/usr/bin/python
# Classification (U)

"""Program:  rabbitmq_init.py

    Description:  Unit testing of rabbitmq.__init__ in rabbitmq_class.py.

    Usage:
        test/unit/rabbitmq_class/rabbitmq_init.py

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


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_with_data -> Test other attributes with data.
        test_default -> Test with minimum number of arguments.

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

    @mock.patch("rabbitmq_class.pika")
    def test_with_data(self, mock_pika):

        """Function:  test_with_data

        Description:  Test __init__ method with all arguments.

        Arguments:

        """

        mock_pika.PlainCredentials.return_value = "PlainCredentials"
        mock_pika.ConnectionParameters.return_value = "ConnectionParameters"
        rmq = rabbitmq_class.RabbitMQ(self.name, "xxxxx", self.host, self.port)

        self.assertEqual((rmq.name, rmq.host, rmq.port, rmq.connection),
                         (self.name, self.host, self.port, None))

    @mock.patch("rabbitmq_class.pika")
    def test_default(self, mock_pika):

        """Function:  test_default

        Description:  Test __init__ method with default arguments.

        Arguments:

        """

        mock_pika.PlainCredentials.return_value = "PlainCredentials"
        mock_pika.ConnectionParameters.return_value = "ConnectionParameters"
        rmq = rabbitmq_class.RabbitMQ(self.name, "xxxxx")

        self.assertEqual((rmq.name, rmq.host, rmq.port, rmq.connection),
                         (self.name, "localhost", 5672, None))


if __name__ == "__main__":
    unittest.main()
