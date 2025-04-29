# Classification (U)

"""Program:  rabbitmqpub_queue_count.py

    Description:  Unit test of rabbitmqpub.check_confirm in rabbitmq_class.py.

    Usage:
        test/unit/rabbitmq_class/rabbitmqpub_queue_count.py

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


class Method():                                         # pylint:disable=R0903

    """Class:  Method

    Description:  Class stub holder for pika class.

    Methods:
        __init__

    """

    def __init__(self):

        """Function:  __init__

        Description:  Initialization of Method class.

        Arguments:

        """

        self.message_count = 2


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_queue_count

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
    def test_queue_count(self, mock_pika):

        """Function:  test_queue_count

        Description:  Test of the queue_count method.

        Arguments:

        """

        mock_pika.PlainCredentials.return_value = "PlainCredentials"
        mock_pika.ConnectionParameters.return_value = "ConnectionParameters"
        rmq = rabbitmq_class.RabbitMQPub(self.name, "xxxxx")
        rmq.queue = Method()

        self.assertEqual(rmq.queue_count(), 2)


if __name__ == "__main__":
    unittest.main()
