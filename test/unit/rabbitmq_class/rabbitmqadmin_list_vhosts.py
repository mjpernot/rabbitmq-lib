# Classification (U)

"""Program:  rabbitmqadmin_list_vhosts.py

    Description:  Unit testing of RabbitMQAdmin.list_vhosts in
        rabbitmq_class.py.

    Usage:
        test/unit/rabbitmq_class/rabbitmqadmin_list_vhosts.py

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
import rabbitmq_class                           # pylint:disable=E0401,C0413
import version                                  # pylint:disable=E0401,C0413

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
        self.results = {"key": "value"}

    @mock.patch("rabbitmq_class.RabbitMQBase.api_get")
    def test_basic(self, mock_get):

        """Function:  test_basic

        Description:  Test with basic set up.

        Arguments:

        """

        mock_get.return_value = self.data

        self.assertEqual(self.rmq.list_vhosts(), self.results)


if __name__ == "__main__":
    unittest.main()
