# Classification (U)

"""Program:  rabbitmqpub_dropqueue.py

    Description:  Unit test of rabbitmqpub.drop_queue in rabbitmq_class.py.

    Usage:
        test/unit/rabbitmq_class/rabbitmqpub_dropqueue.py

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


class DropQueue(object):

    """Class:  DropQueue

    Description:  Class stub holder for pika class.

    Methods:
        __init__
        basic_publish

    """

    def __init__(self):

        """Function:  __init__

        Description:  Stub holder for __init__ function.

        Arguments:

        """

        self.queue = None
        self.if_unused = None
        self.if_empty = None

    def queue_delete(self, queue, if_unused, if_empty):

        """Function:  queue_delete

        Description:  Stub holder for queue_delete function.

        Arguments:
            queue
            if_unused
            if_empty

        """

        self.queue = queue
        self.if_unused = if_unused
        self.if_empty = if_empty

        return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_drop_queue

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
    def test_drop_queue(self, mock_pika):

        """Function:  test_drop_queue

        Description:  Test drop_queue method.

        Arguments:

        """

        mock_pika.PlainCredentials.return_value = "PlainCredentials"
        mock_pika.ConnectionParameters.return_value = "ConnectionParameters"
        mock_pika.BasicProperties.return_value = True
        rmq = rabbitmq_class.RabbitMQPub(self.name, "xxxxx")
        rmq.channel = DropQueue()

        self.assertFalse(rmq.drop_queue())


if __name__ == "__main__":
    unittest.main()
