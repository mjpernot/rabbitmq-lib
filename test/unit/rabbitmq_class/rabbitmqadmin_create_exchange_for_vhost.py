# Classification (U)

"""Program:  rabbitmqadmin_create_exchange_for_vhost.py

    Description:  Unit testing of RabbitMQAdmin.create_exchange_for_vhost in
        rabbitmq_class.py.

    Usage:
        test/unit/rabbitmq_class/rabbitmqadmin_create_exchange_for_vhost.py

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
        self.body = {"type": "direct"}
        self.vhost = "VirtualHost"
        self.exchange = "ExchangeName"

    @mock.patch("rabbitmq_class.RabbitMQBase.api_put")
    def test_basic(self, mock_put):

        """Function:  test_basic

        Description:  Test with basic set up.

        Arguments:

        """

        mock_put.return_value = True

        self.assertFalse(
            self.rmq.create_exchange_for_vhost(
                self.exchange, self.vhost, self.body))


if __name__ == "__main__":
    unittest.main()
