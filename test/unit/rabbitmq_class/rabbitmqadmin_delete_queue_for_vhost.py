# Classification (U)

"""Program:  rabbitmqadmin_delete_queue_for_vhost.py

    Description:  Unit testing of RabbitMQAdmin.delete_queue_for_vhost in
        rabbitmq_class.py.

    Usage:
        test/unit/rabbitmq_class/rabbitmqadmin_delete_queue_for_vhost.py

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
        test_both
        test_if_unused
        test_if_empty
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
        self.qname = "QueueName"
        self.vhost = "VhostName"
        self.if_unused = False
        self.if_empty = False

    @mock.patch("rabbitmq_class.RabbitMQBase.api_delete")
    def test_both(self, mock_delete):

        """Function:  test_both

        Description:  Test with if_unused and if_empty set to False.

        Arguments:

        """

        mock_delete.return_value = True

        self.assertFalse(
            self.rmq.delete_queue_for_vhost(
                self.qname, self.vhost, if_unused=self.if_unused,
                if_empty=self.if_empty))

    @mock.patch("rabbitmq_class.RabbitMQBase.api_delete")
    def test_if_unused(self, mock_delete):

        """Function:  test_if_unused

        Description:  Test with if_unused set to False.

        Arguments:

        """

        mock_delete.return_value = True

        self.assertFalse(
            self.rmq.delete_queue_for_vhost(
                self.qname, self.vhost, if_unused=self.if_unused))

    @mock.patch("rabbitmq_class.RabbitMQBase.api_delete")
    def test_if_empty(self, mock_delete):

        """Function:  test_if_empty

        Description:  Test with if_empty set to False.

        Arguments:

        """

        mock_delete.return_value = True

        self.assertFalse(
            self.rmq.delete_queue_for_vhost(
                self.qname, self.vhost, if_empty=self.if_empty))

    @mock.patch("rabbitmq_class.RabbitMQBase.api_delete")
    def test_basic(self, mock_delete):

        """Function:  test_basic

        Description:  Test with basic set up.

        Arguments:

        """

        mock_delete.return_value = True

        self.assertFalse(
            self.rmq.delete_queue_for_vhost(self.qname, self.vhost))


if __name__ == "__main__":
    unittest.main()
