# Classification (U)

"""Program:  rabbitmqbase_api_get.py

    Description:  Unit testing of RabbitMQBase.api_get in rabbitmq_class.py.

    Usage:
        test/unit/rabbitmq_class/rabbitmqbase_api_get.py

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
        test_headers
        test_basic

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.name = "UserName"
        self.japd = "Japd"
        self.url_cmd = "Url_Command"

    @mock.patch("rabbitmq_class.RabbitMQBase.get",
                mock.Mock(return_value=True))
    def test_headers(self):

        """Function:  test_headers

        Description:  Test with headers passed in.

        Arguments:

        """

        rmq = rabbitmq_class.RabbitMQBase(self.name, self.japd)
        rmq.api_get(self.url_cmd, headers=rmq.headers)

    @mock.patch("rabbitmq_class.RabbitMQBase.get",
                mock.Mock(return_value=True))
    def test_basic(self):

        """Function:  test_basic

        Description:  Test with basic set up.

        Arguments:

        """

        rmq = rabbitmq_class.RabbitMQBase(self.name, self.japd)
        rmq.api_get(self.url_cmd)


if __name__ == "__main__":
    unittest.main()
