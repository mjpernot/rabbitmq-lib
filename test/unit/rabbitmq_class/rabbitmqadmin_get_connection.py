#!/usr/bin/python
# Classification (U)

"""Program:  rabbitmqadmin_get_connection.py

    Description:  Unit testing of RabbitMQAdmin.get_connection in
        rabbitmq_class.py.

    Usage:
        test/unit/rabbitmq_class/rabbitmqadmin_get_connection.py

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
        setUp
        test_basic

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.name = "UserName"
        self.japd = "japd"
        self.rmq = rabbitmq_class.RabbitMQAdmin(self.name, self.japd)
        self.data = {"key": "value"}
        self.connection = "ConnectionName"
        self.results = {"key": "value"}

    @mock.patch("rabbitmq_class.RabbitMQBase.api_get")
    def test_basic(self, mock_get):

        """Function:  test_basic

        Description:  Test with basic set up.

        Arguments:

        """

        mock_get.return_value = self.data

        self.assertEqual(
            self.rmq.get_connection(self.connection), self.results)


if __name__ == "__main__":
    unittest.main()
