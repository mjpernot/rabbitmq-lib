# Classification (U)

"""Program:  rabbitmqpub_clearqueue.py

    Description:  Unit test of rabbitmqpub.clear_queue in rabbitmq_class.py.

    Usage:
        test/unit/rabbitmq_class/rabbitmqpub_clearqueue.py

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


class ClearQueue():                                     # pylint:disable=R0903

    """Class:  ClearQueue

    Description:  Class stub holder for pika class.

    Methods:
        __init__
        queue_purge

    """

    def __init__(self):

        """Function:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.queue = None

    def queue_purge(self, queue):

        """Function:  queue_purge

        Description:  Stub holder for queue_purge function.

        Arguments:
            queue

        """

        self.queue = queue

        return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_clear_queue

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
    def test_clear_queue(self, mock_pika):

        """Function:  test_clear_queue

        Description:  Test clear_queue method.

        Arguments:

        """

        mock_pika.PlainCredentials.return_value = "PlainCredentials"
        mock_pika.ConnectionParameters.return_value = "ConnectionParameters"
        mock_pika.BasicProperties.return_value = True
        rmq = rabbitmq_class.RabbitMQPub(self.name, "xxxxx")
        rmq.channel = ClearQueue()

        self.assertFalse(rmq.clear_queue())


if __name__ == "__main__":
    unittest.main()
