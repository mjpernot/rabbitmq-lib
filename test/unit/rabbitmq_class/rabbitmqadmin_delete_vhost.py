# Classification (U)

"""Program:  rabbitmqadmin_delete_vhost.py

    Description:  Unit testing of RabbitMQAdmin.delete_vhost in
        rabbitmq_class.py.

    Usage:
        test/unit/rabbitmq_class/rabbitmqadmin_delete_vhost.py

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
        self.vhost = "VirtualHost"

    @mock.patch("rabbitmq_class.RabbitMQBase.api_delete")
    def test_basic(self, mock_delete):

        """Function:  test_basic

        Description:  Test with basic set up.

        Arguments:

        """

        mock_delete.return_value = True

        self.assertFalse(self.rmq.delete_vhost(self.vhost))


if __name__ == "__main__":
    unittest.main()
