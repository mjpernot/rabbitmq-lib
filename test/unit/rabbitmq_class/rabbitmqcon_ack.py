# Classification (U)

"""Program:  rabbitmqcon_ack.py

    Description:  Unit test of rabbitmqcon.ack in rabbitmq_class.py.

    Usage:
        test/unit/rabbitmq_class/rabbitmqcon_ack.py

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


class Ack():                                            # pylint:disable=R0903

    """Class:  Ack

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

        self.delivery_tag = None

    def basic_ack(self, delivery_tag):

        """Function:  basic_ack

        Description:  Stub holder for basic_ack function.

        Arguments:
            delivery_tag

        """

        self.delivery_tag = delivery_tag

        return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_ack

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
    def test_ack(self, mock_pika):

        """Function:  test_ack

        Description:  Test ack method.

        Arguments:

        """

        mock_pika.PlainCredentials.return_value = "PlainCredentials"
        mock_pika.ConnectionParameters.return_value = "ConnectionParameters"
        mock_pika.BasicProperties.return_value = True
        rmq = rabbitmq_class.RabbitMQCon(self.name, "xxxxx")
        rmq.channel = Ack()

        self.assertFalse(rmq.ack("tag"))


if __name__ == "__main__":
    unittest.main()
