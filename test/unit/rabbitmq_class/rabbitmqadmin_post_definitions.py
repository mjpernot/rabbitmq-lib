# Classification (U)

"""Program:  rabbitmqadmin_post_definitions.py

    Description:  Unit testing of RabbitMQAdmin.post_definitions in
        rabbitmq_class.py.

    Usage:
        test/unit/rabbitmq_class/rabbitmqadmin_post_definitions.py

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
        self.definitions = {"key": "value"}

    @mock.patch("rabbitmq_class.RabbitMQBase.api_post")
    def test_basic(self, mock_post):

        """Function:  test_basic

        Description:  Test with basic set up.

        Arguments:

        """

        mock_post.return_value = True

        self.assertFalse(self.rmq.post_definitions(self.definitions))


if __name__ == "__main__":
    unittest.main()
