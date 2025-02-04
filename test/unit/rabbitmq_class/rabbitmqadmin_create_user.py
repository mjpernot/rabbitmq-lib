# Classification (U)

"""Program:  rabbitmqadmin_create_user.py

    Description:  Unit testing of RabbitMQAdmin.create_user in
        rabbitmq_class.py.

    Usage:
        test/unit/rabbitmq_class/rabbitmqadmin_create_user.py

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
        test_tags
        test_no_tags
        test_japd_and_hash
        test_japd_hash_only
        test_no_japd
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
        self.ujapd = "UserJapd"
        self.japd_hash = "UserHash"
        self.tags = ["administrator"]

    @mock.patch("rabbitmq_class.RabbitMQBase.api_put")
    def test_tags(self, mock_put):

        """Function:  test_tags

        Description:  Test with tags passed.

        Arguments:

        """

        mock_put.return_value = True

        self.assertFalse(
            self.rmq.create_user(self.uname, self.ujapd, tags=self.tags))

    @mock.patch("rabbitmq_class.RabbitMQBase.api_put")
    def test_no_tags(self, mock_put):

        """Function:  test_no_tags

        Description:  Test with no tags passed.

        Arguments:

        """

        mock_put.return_value = True

        self.assertFalse(self.rmq.create_user(self.uname, self.ujapd, tags=[]))

    @mock.patch("rabbitmq_class.RabbitMQBase.api_put")
    def test_japd_and_hash(self, mock_put):

        """Function:  test_japd_and_hash

        Description:  Test with user japd and japd hash passed.

        Arguments:

        """

        mock_put.return_value = True

        self.assertFalse(
            self.rmq.create_user(
                self.uname, self.ujapd, japd_hash=self.japd_hash))

    @mock.patch("rabbitmq_class.RabbitMQBase.api_put")
    def test_japd_hash_only(self, mock_put):

        """Function:  test_japd_hash_only

        Description:  Test with only user japd hash passed.

        Arguments:

        """

        mock_put.return_value = True

        self.assertFalse(
            self.rmq.create_user(self.uname, "", japd_hash=self.japd_hash))

    @mock.patch("rabbitmq_class.RabbitMQBase.api_put")
    def test_no_japd(self, mock_put):

        """Function:  test_no_japd

        Description:  Test with no user japd passed.

        Arguments:

        """

        mock_put.return_value = True

        self.assertFalse(self.rmq.create_user(self.uname, ""))

    @mock.patch("rabbitmq_class.RabbitMQBase.api_put")
    def test_basic(self, mock_put):

        """Function:  test_basic

        Description:  Test with basic set up.

        Arguments:

        """

        mock_put.return_value = True

        self.assertFalse(self.rmq.create_user(self.uname, self.ujapd))


if __name__ == "__main__":
    unittest.main()
