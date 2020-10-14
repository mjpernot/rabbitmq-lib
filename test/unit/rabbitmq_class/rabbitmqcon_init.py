#!/usr/bin/python
# Classification (U)

"""Program:  rabbitmqcon_init.py

    Description:  Unit testing of rabbitmqcon.__init__ in rabbitmq_class.py.

    Usage:
        test/unit/rabbitmq_class/rabbitmqcon_init.py

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
        test_with_data -> Test other attributes with data.
        test_default -> Test with minimum number of arguments.

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
        self.no_ack = True

    @mock.patch("rabbitmq_class.pika")
    def test_with_data(self, mock_pika):

        """Function:  test_with_data

        Description:  Test __init__ method with all arguments.

        Arguments:

        """

        mock_pika.PlainCredentials.return_value = "PlainCredentials"
        mock_pika.ConnectionParameters.return_value = "ConnectionParameters"
        rmq = rabbitmq_class.RabbitMQCon(
            self.name, "xxxxx", self.host, self.port,
            exchange_name=self.exchange_name, queue_name=self.queue_name,
            routing_key=self.routing_key, auto_delete=self.auto_delete,
            no_ack=self.no_ack)

        self.assertEqual((rmq.name, rmq.host, rmq.port, rmq.exchange,
                          rmq.exchange_type, rmq.queue_name, rmq.routing_key,
                          rmq.x_durable, rmq.q_durable, rmq.auto_delete,
                          rmq.no_ack),
                         (self.name, self.host, 5555, self.exchange_name,
                          "direct", self.queue_name, self.routing_key,
                          True, True, self.auto_delete, self.no_ack))

    @mock.patch("rabbitmq_class.pika")
    def test_default(self, mock_pika):

        """Function:  test_default

        Description:  Test __init__ method with default arguments.

        Arguments:

        """

        mock_pika.PlainCredentials.return_value = "PlainCredentials"
        mock_pika.ConnectionParameters.return_value = "ConnectionParameters"
        rmq = rabbitmq_class.RabbitMQCon(self.name, "xxxxx")

        self.assertEqual((rmq.name, rmq.host, rmq.port, rmq.exchange,
                          rmq.exchange_type, rmq.queue_name, rmq.routing_key,
                          rmq.x_durable, rmq.q_durable, rmq.auto_delete,
                          rmq.no_ack),
                         (self.name, "localhost", 5672, "", "direct", "", "",
                          True, True, False, False))


if __name__ == "__main__":
    unittest.main()
