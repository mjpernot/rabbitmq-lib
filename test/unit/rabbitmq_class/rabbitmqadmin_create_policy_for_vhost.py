# Classification (U)

"""Program:  rabbitmqadmin_create_policy_for_vhost.py

    Description:  Unit testing of RabbitMQAdmin.create_policy_for_vhost in
        rabbitmq_class.py.

    Usage:
        test/unit/rabbitmq_class/rabbitmqadmin_create_policy_for_vhost.py

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
        test_apply_to
        test_priority
        test_pattern
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
        self.pname = "PolicyName"
        self.vhost = "VhostName"
        self.definition = {"ha-mode": "all"}
        self.pattern = 'Name.*'
        self.priority = 1
        self.apply_to = "all"

    @mock.patch("rabbitmq_class.RabbitMQBase.api_put")
    def test_apply_to(self, mock_put):

        """Function:  test_apply_to

        Description:  Test with apply_to passed.

        Arguments:

        """

        mock_put.return_value = True

        self.assertFalse(
            self.rmq.create_policy_for_vhost(
                self.vhost, self.pname, self.definition,
                apply_to=self.apply_to))

    @mock.patch("rabbitmq_class.RabbitMQBase.api_put")
    def test_priority(self, mock_put):

        """Function:  test_priority

        Description:  Test with priority passed.

        Arguments:

        """

        mock_put.return_value = True

        self.assertFalse(
            self.rmq.create_policy_for_vhost(
                self.vhost, self.pname, self.definition,
                priority=self.priority))

    @mock.patch("rabbitmq_class.RabbitMQBase.api_put")
    def test_pattern(self, mock_put):

        """Function:  test_pattern

        Description:  Test with pattern passed.

        Arguments:

        """

        mock_put.return_value = True

        self.assertFalse(
            self.rmq.create_policy_for_vhost(
                self.vhost, self.pname, self.definition, pattern=self.pattern))

    @mock.patch("rabbitmq_class.RabbitMQBase.api_put")
    def test_basic(self, mock_put):

        """Function:  test_basic

        Description:  Test with basic set up.

        Arguments:

        """

        mock_put.return_value = True

        self.assertFalse(
            self.rmq.create_policy_for_vhost(
                self.vhost, self.pname, self.definition))


if __name__ == "__main__":
    unittest.main()
