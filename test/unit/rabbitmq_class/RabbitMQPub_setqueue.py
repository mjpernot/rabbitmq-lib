#!/usr/bin/python
# Classification (U)

"""Program:  RabbitMQPub_setqueue.py

    Description:  Unit test of RabbitMQPub.set_queue in rabbitmq_class.py.

    Usage:
        test/unit/rabbitmq_class/RabbitMQPub_setqueue.py

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
        setUp -> Initialize testing environment.
        test_setup_queue -> Test setup_queue method.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.name = None
        self.host = "ServerName"
        self.port = 5555
        self.connection = None
        self.exchange_name = "Exchange_Name"
        self.queue_name = "Queue_Name"
        self.routing_key = "Route_Key"
        self.auto_delete = True

    @mock.patch("rabbitmq_class.RabbitMQPub.check_confirm")
    @mock.patch("rabbitmq_class.RabbitMQPub.bind_queue")
    @mock.patch("rabbitmq_class.RabbitMQPub.create_queue")
    @mock.patch("rabbitmq_class.RabbitMQPub.setup_exchange")
    @mock.patch("rabbitmq_class.pika")
    def test_setup_queue(self, mock_pika, mock_setup, mock_create, mock_bind,
                         mock_check):

        """Function:  test_setup_queue

        Description:  Test setup_queue method.

        Arguments:

        """

        mock_pika.PlainCredentials.return_value = "PlainCredentials"
        mock_pika.ConnectionParameters.return_value = "ConnectionParameters"
        mock_setup.return_value = True
        mock_create.return_value = True
        mock_bind.return_value = True
        mock_check.return_value = True
        rmq = rabbitmq_class.RabbitMQPub(self.name, "xxxxx")

        self.assertFalse(rmq.setup_queue())


if __name__ == "__main__":
    unittest.main()
