#!/usr/bin/python
# Classification (U)

"""Program:  rabbitmqadmin_create_queue_for_vhost.py

    Description:  Unit testing of RabbitMQAdmin.create_queue_for_vhost in
        rabbitmq_class.py.

    Usage:
        test/unit/rabbitmq_class/rabbitmqadmin_create_queue_for_vhost.py

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
        test_body
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
        self.body = {"auto_delete": False, "durable": True, "arguments": {},
                     "node": "rabbit@rabbit1"}
        self.body2 = {}

    @mock.patch("rabbitmq_class.RabbitMQBase.api_put")
    def test_body(self, mock_put):

        """Function:  test_body

        Description:  Test with empty body.

        Arguments:

        """

        mock_put.return_value = True

        self.assertFalse(
            self.rmq.create_queue_for_vhost(
                self.qname, self.vhost, self.body2))

    @mock.patch("rabbitmq_class.RabbitMQBase.api_put")
    def test_basic(self, mock_put):

        """Function:  test_basic

        Description:  Test with basic set up.

        Arguments:

        """

        mock_put.return_value = True

        self.assertFalse(
            self.rmq.create_queue_for_vhost(self.qname, self.vhost, self.body))


if __name__ == "__main__":
    unittest.main()
