# Classification (U)

"""Program:  rabbitmqpub_checkconfirm.py

    Description:  Unit test of rabbitmqpub.check_confirm in rabbitmq_class.py.

    Usage:
        test/unit/rabbitmq_class/rabbitmqpub_checkconfirm.py

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


class CheckConfirm():                                   # pylint:disable=R0903

    """Class:  CheckConfirm

    Description:  Class stub holder for pika class.

    Methods:
        confirm_delivery

    """

    def confirm_delivery(self):

        """Function:  confirm_delivery

        Description:  Stub holder for confirm_delivery function.

        Arguments:

        """

        return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_close_channel

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
    def test_close_channel(self, mock_pika):

        """Function:  test_close_channel

        Description:  Test close_channel method.

        Arguments:

        """

        mock_pika.PlainCredentials.return_value = "PlainCredentials"
        mock_pika.ConnectionParameters.return_value = "ConnectionParameters"
        rmq = rabbitmq_class.RabbitMQPub(self.name, "xxxxx")
        rmq.channel = CheckConfirm()

        self.assertFalse(rmq.check_confirm())


if __name__ == "__main__":
    unittest.main()
