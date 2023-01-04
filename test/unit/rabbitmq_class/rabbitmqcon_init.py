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
        test_multiple_node
        test_single_node
        test_heartbeat_set
        test_heartbeat_default
        test_with_data
        test_default

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
        self.host_list = ["host1:5671", "host2:5672"]
        self.params_list = ["ConnectionParameters", "ConnectionParameters"]

    @mock.patch("rabbitmq_class.pika")
    def test_multiple_node(self, mock_pika):

        """Function:  test_multiple_node

        Description:  Test with multiple node connection.

        Arguments:

        """

        mock_pika.PlainCredentials.return_value = "PlainCredentials"
        mock_pika.ConnectionParameters.return_value = "ConnectionParameters"
        rmq = rabbitmq_class.RabbitMQCon(
            self.name, "xxxxx", self.host, self.port,
            exchange_name=self.exchange_name, queue_name=self.queue_name,
            routing_key=self.routing_key, auto_delete=self.auto_delete,
            no_ack=self.no_ack, host_list=self.host_list)

        self.assertEqual(rmq.params, self.params_list)

    @mock.patch("rabbitmq_class.pika")
    def test_single_node(self, mock_pika):

        """Function:  test_single_node

        Description:  Test with single node connection.

        Arguments:

        """

        mock_pika.PlainCredentials.return_value = "PlainCredentials"
        mock_pika.ConnectionParameters.return_value = "ConnectionParameters"
        rmq = rabbitmq_class.RabbitMQCon(
            self.name, "xxxxx", self.host, self.port,
            exchange_name=self.exchange_name, queue_name=self.queue_name,
            routing_key=self.routing_key, auto_delete=self.auto_delete,
            no_ack=self.no_ack)

        self.assertEqual(rmq.params, "ConnectionParameters")

    @mock.patch("rabbitmq_class.pika")
    def test_heartbeat_set(self, mock_pika):

        """Function:  test_heartbeat_set

        Description:  Test with set heartbeat value.

        Arguments:

        """

        mock_pika.PlainCredentials.return_value = "PlainCredentials"
        mock_pika.ConnectionParameters.return_value = "ConnectionParameters"
        rmq = rabbitmq_class.RabbitMQCon(
            self.name, "xxxxx", self.host, self.port,
            exchange_name=self.exchange_name, queue_name=self.queue_name,
            routing_key=self.routing_key, auto_delete=self.auto_delete,
            no_ack=self.no_ack, heartbeat=120)

        self.assertEqual(rmq.heartbeat, 120)

    @mock.patch("rabbitmq_class.pika")
    def test_heartbeat_default(self, mock_pika):

        """Function:  test_heartbeat_default

        Description:  Test with default heartbeat value.

        Arguments:

        """

        mock_pika.PlainCredentials.return_value = "PlainCredentials"
        mock_pika.ConnectionParameters.return_value = "ConnectionParameters"
        rmq = rabbitmq_class.RabbitMQCon(
            self.name, "xxxxx", self.host, self.port,
            exchange_name=self.exchange_name, queue_name=self.queue_name,
            routing_key=self.routing_key, auto_delete=self.auto_delete,
            no_ack=self.no_ack)

        self.assertEqual(rmq.heartbeat, 60)

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

        self.assertEqual(
            (rmq.name, rmq.host, rmq.port, rmq.exchange, rmq.exchange_type,
             rmq.queue_name, rmq.routing_key, rmq.x_durable, rmq.q_durable,
             rmq.auto_delete, rmq.no_ack),
            (self.name, self.host, 5555, self.exchange_name, "direct",
             self.queue_name, self.routing_key, True, True, self.auto_delete,
             self.no_ack))

    @mock.patch("rabbitmq_class.pika")
    def test_default(self, mock_pika):

        """Function:  test_default

        Description:  Test __init__ method with default arguments.

        Arguments:

        """

        mock_pika.PlainCredentials.return_value = "PlainCredentials"
        mock_pika.ConnectionParameters.return_value = "ConnectionParameters"
        rmq = rabbitmq_class.RabbitMQCon(self.name, "xxxxx")

        self.assertEqual(
            (rmq.name, rmq.host, rmq.port, rmq.exchange, rmq.exchange_type,
             rmq.queue_name, rmq.routing_key, rmq.x_durable, rmq.q_durable,
             rmq.auto_delete, rmq.no_ack),
            (self.name, "localhost", 5672, "", "direct", "", "", True, True,
             False, False))


if __name__ == "__main__":
    unittest.main()
