#!/usr/bin/python
# Classification (U)

"""Program:  RabbitMQPub_init.py

    Description:  Unit testing of RabbitMQPub.__init__ in rabbitmq_class.py.

    Usage:
        test/unit/rabbitmq_class/RabbitMQPub_init.py

    Arguments:
        None

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

    Super-Class:  unittest.TestCase

    Sub-Classes:  None

    Methods:
        setUp -> Initialize testing environment.
        test_with_data -> Test other attributes with data.
        test_default -> Test with minimum number of arguments.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:
            None

        """

        self.name = None
        self.host = "ServerName"
        self.port = 5555
        self.connection = None
        self.exchange_name = "Exchange_Name"
        self.queue_name = "Queue_Name"
        self.routing_key = "Route_Key"
        self.auto_delete = True

    @mock.patch("rabbitmq_class.pika")
    def test_with_data(self, mock_pika):

        """Function:  test_with_data

        Description:  Test __init__ method with all arguments.

        Arguments:
            None

        """

        mock_pika.PlainCredentials.return_value = "PlainCredentials"
        mock_pika.ConnectionParameters.return_value = "ConnectionParameters"
        rq = rabbitmq_class.RabbitMQPub(self.name, "pwd", self.host, self.port,
                                        exchange_name=self.exchange_name,
                                        queue_name=self.queue_name,
                                        routing_key=self.routing_key,
                                        auto_delete=self.auto_delete)

        self.assertEqual((rq.name, rq.host, rq.port, rq.exchange,
                          rq.exchange_type, rq.queue_name, rq.routing_key,
                          rq.x_durable, rq.q_durable, rq.auto_delete),
                         (self.name, self.host, 5555, self.exchange_name,
                          "direct", self.queue_name, self.routing_key,
                          True, True, self.auto_delete))

    @mock.patch("rabbitmq_class.pika")
    def test_default(self, mock_pika):

        """Function:  test_default

        Description:  Test __init__ method with default arguments.

        Arguments:
            None

        """

        mock_pika.PlainCredentials.return_value = "PlainCredentials"
        mock_pika.ConnectionParameters.return_value = "ConnectionParameters"
        rq = rabbitmq_class.RabbitMQPub(self.name, "pwd")

        self.assertEqual((rq.name, rq.host, rq.port, rq.exchange,
                          rq.exchange_type, rq.queue_name, rq.routing_key,
                          rq.x_durable, rq.q_durable, rq.auto_delete),
                         (self.name, "localhost", 5672, "", "direct", "", "",
                          True, True, False))


if __name__ == "__main__":
    unittest.main()
