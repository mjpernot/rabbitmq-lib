# Classification (U)

"""Program:  rabbitmqpub_unbindqueue.py

    Description:  Unit test of rabbitmqpub.unbind_queue in rabbitmq_class.py.

    Usage:
        test/unit/rabbitmq_class/rabbitmqpub_unbindqueue.py

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


class UnbindQueue():                                    # pylint:disable=R0903

    """Class:  UnbindQueue

    Description:  Class stub holder for pika class.

    Methods:
        __init__
        queue_unbind

    """

    def __init__(self):

        """Function:  __init__

        Description:  Stub holder for __init__ function.

        Arguments:

        """

        self.queue = None
        self.exchange = None
        self.routing_key = None

    def queue_unbind(self, queue, exchange, routing_key):

        """Function:  queue_unbind

        Description:  Stub holder for queue_unbind function.

        Arguments:
            queue
            exchange
            routing_key

        """

        self.queue = queue
        self.exchange = exchange
        self.routing_key = routing_key

        return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_unbind_queue

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
        self.body = "Message_Body"

    @mock.patch("rabbitmq_class.pika")
    def test_unbind_queue(self, mock_pika):

        """Function:  test_unbind_queue

        Description:  Test unbind_queue method.

        Arguments:

        """

        mock_pika.PlainCredentials.return_value = "PlainCredentials"
        mock_pika.ConnectionParameters.return_value = "ConnectionParameters"
        mock_pika.BasicProperties.return_value = True
        rmq = rabbitmq_class.RabbitMQPub(self.name, "xxxxx")
        rmq.channel = UnbindQueue()

        self.assertFalse(rmq.unbind_queue())


if __name__ == "__main__":
    unittest.main()
