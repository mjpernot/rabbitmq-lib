# Classification (U)

"""Program:  rabbitmqbase_api_delete.py

    Description:  Unit testing of RabbitMQBase.api_delete in rabbitmq_class.py.

    Usage:
        test/unit/rabbitmq_class/rabbitmqbase_api_delete.py

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
import rabbitmq_class
import version

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

    @mock.patch("rabbitmq_class.RabbitMQBase.delete",
                mock.Mock(return_value=True))
    def test_headers(self):

        """Function:  test_headers

        Description:  Test with headers passed in.

        Arguments:

        """

        rmq = rabbitmq_class.RabbitMQBase(self.name, self.japd)
        rmq.api_delete(self.url_cmd, headers=rmq.headers)

    @mock.patch("rabbitmq_class.RabbitMQBase.delete",
                mock.Mock(return_value=True))
    def test_basic(self):

        """Function:  test_basic

        Description:  Test with basic set up.

        Arguments:

        """

        rmq = rabbitmq_class.RabbitMQBase(self.name, self.japd)
        rmq.api_delete(self.url_cmd)


if __name__ == "__main__":
    unittest.main()
