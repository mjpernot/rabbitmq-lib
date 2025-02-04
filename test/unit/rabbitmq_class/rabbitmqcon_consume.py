# Classification (U)

"""Program:  rabbitmqcon_consume.py

    Description:  Unit test of rabbitmqcon.consume in rabbitmq_class.py.

    Usage:
        test/unit/rabbitmq_class/rabbitmqcon_consume.py

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


class Consume2():                                       # pylint:disable=R0903

    """Class:  Consume2

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

        self.func_call = None
        self.queue_name = None
        self.auto_ack = None

    def basic_consume(self, queue_name, func_call, auto_ack):

        """Function:  basic_consume

        Description:  Stub holder for basic_consume function.

        Arguments:

        """

        self.func_call = func_call
        self.queue_name = queue_name
        self.auto_ack = auto_ack

        return True


class Consume():                                        # pylint:disable=R0903

    """Class:  Consume

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

        self.func_call = None
        self.queue_name = None
        self.no_ack = None

    def basic_consume(self, func_call, queue_name, no_ack):

        """Function:  basic_consume

        Description:  Stub holder for basic_consume function.

        Arguments:

        """

        self.func_call = func_call
        self.queue_name = queue_name
        self.no_ack = no_ack

        return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_pika_pre
        test_pika_post
        test_queue_arg
        test_consume

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
    def test_pika_pre(self, mock_pika):

        """Function:  test_pika_pre

        Description:  Test with Pika version greater than 1.0.0.

        Arguments:

        """

        mock_pika.PlainCredentials.return_value = "PlainCredentials"
        mock_pika.ConnectionParameters.return_value = "ConnectionParameters"
        mock_pika.BasicProperties.return_value = True
        rmq = rabbitmq_class.RabbitMQCon(self.name, "xxxxx")
        rmq.channel = Consume()
        mock_pika.__version__ = "0.11.0"

        self.assertTrue(rmq.consume("func_call"))

    @mock.patch("rabbitmq_class.pika")
    def test_pika_post(self, mock_pika):

        """Function:  test_pika_post

        Description:  Test with Pika version greater than 1.0.0.

        Arguments:

        """

        mock_pika.PlainCredentials.return_value = "PlainCredentials"
        mock_pika.ConnectionParameters.return_value = "ConnectionParameters"
        mock_pika.BasicProperties.return_value = True
        rmq = rabbitmq_class.RabbitMQCon(self.name, "xxxxx")
        rmq.channel = Consume2()
        mock_pika.__version__ = "1.2.0"

        self.assertTrue(rmq.consume("func_call"))

    @mock.patch("rabbitmq_class.pika")
    def test_queue_arg(self, mock_pika):

        """Function:  test_queue_arg

        Description:  Test with queue argument.

        Arguments:

        """

        mock_pika.PlainCredentials.return_value = "PlainCredentials"
        mock_pika.ConnectionParameters.return_value = "ConnectionParameters"
        mock_pika.BasicProperties.return_value = True
        rmq = rabbitmq_class.RabbitMQCon(self.name, "xxxxx")
        rmq.channel = Consume2()
        mock_pika.__version__ = "1.2.0"

        self.assertTrue(rmq.consume("func_call", queue="queue_name"))

    @mock.patch("rabbitmq_class.pika")
    def test_consume(self, mock_pika):

        """Function:  test_consume

        Description:  Test consume method.

        Arguments:

        """

        mock_pika.PlainCredentials.return_value = "PlainCredentials"
        mock_pika.ConnectionParameters.return_value = "ConnectionParameters"
        mock_pika.BasicProperties.return_value = True
        rmq = rabbitmq_class.RabbitMQCon(self.name, "xxxxx")
        rmq.channel = Consume2()
        mock_pika.__version__ = "1.2.0"

        self.assertTrue(rmq.consume("func_call"))


if __name__ == "__main__":
    unittest.main()
