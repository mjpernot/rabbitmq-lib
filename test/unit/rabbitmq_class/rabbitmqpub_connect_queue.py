# Classification (U)

"""Program:  rabbitmqpub_connect_queue.py

    Description:  Unit test of rabbitmqpub.connect_queue in rabbitmq_class.py.

    Usage:
        test/unit/rabbitmq_class/rabbitmqpub_connect_queue.py

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


class ConnectQueue():                                   # pylint:disable=R0903

    """Class:  ConnectQueue

    Description:  Class stub holder for pika class.

    Methods:
        __init__
        queue_declare

    """

    def __init__(self):

        """Function:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.queue = None
        self.durable = None
        self.auto_delete = None

    def queue_declare(self, queue, durable, auto_delete):

        """Function:  queue_declare

        Description:  Stub holder for queue_declare function.

        Arguments:
            queue
            durable
            auto_delete

        """

        self.queue = queue
        self.durable = durable
        self.auto_delete = auto_delete

        return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_create_queue

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

    @mock.patch("rabbitmq_class.pika")
    def test_connect_queue(self, mock_pika):

        """Function:  test_connect_queue

        Description:  Test connecting to queue.

        Arguments:

        """

        mock_pika.PlainCredentials.return_value = "PlainCredentials"
        mock_pika.ConnectionParameters.return_value = "ConnectionParameters"
        rmq = rabbitmq_class.RabbitMQPub(self.name, "xxxxx")
        rmq.channel = ConnectQueue()
        rmq.connect_queue()

        self.assertTrue(rmq.queue)


if __name__ == "__main__":
    unittest.main()
