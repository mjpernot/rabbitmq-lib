# Classification (U)

"""Program:  rabbitmqadmin_create_user_permission.py

    Description:  Unit testing of RabbitMQAdmin.create_user_permission in
        rabbitmq_class.py.

    Usage:
        test/unit/rabbitmq_class/rabbitmqadmin_create_user_permission.py

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
        test_read
        test_write
        test_configure
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
        self.uname = "UserName"
        self.vhost = "VhostName"
        self.configure = 'name2*'
        self.write = 'name3*'
        self.read = 'name4*'

    @mock.patch("rabbitmq_class.RabbitMQBase.api_put")
    def test_read(self, mock_put):

        """Function:  test_read

        Description:  Test with read passed.

        Arguments:

        """

        mock_put.return_value = True

        self.assertFalse(
            self.rmq.create_user_permission(
                self.uname, self.vhost, read=self.read))

    @mock.patch("rabbitmq_class.RabbitMQBase.api_put")
    def test_write(self, mock_put):

        """Function:  test_write

        Description:  Test with write passed.

        Arguments:

        """

        mock_put.return_value = True

        self.assertFalse(
            self.rmq.create_user_permission(
                self.uname, self.vhost, write=self.write))

    @mock.patch("rabbitmq_class.RabbitMQBase.api_put")
    def test_configure(self, mock_put):

        """Function:  test_configure

        Description:  Test with configure passed.

        Arguments:

        """

        mock_put.return_value = True

        self.assertFalse(
            self.rmq.create_user_permission(
                self.uname, self.vhost, configure=self.configure))

    @mock.patch("rabbitmq_class.RabbitMQBase.api_put")
    def test_basic(self, mock_put):

        """Function:  test_basic

        Description:  Test with basic set up.

        Arguments:

        """

        mock_put.return_value = True

        self.assertFalse(
            self.rmq.create_user_permission(self.uname, self.vhost))


if __name__ == "__main__":
    unittest.main()
