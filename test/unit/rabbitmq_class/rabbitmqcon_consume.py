#!/usr/bin/python
# Classification (U)

"""Program:  RabbitMQCon_consume.py

    Description:  Unit test of RabbitMQCon.consume in rabbitmq_class.py.

    Usage:
        test/unit/rabbitmq_class/RabbitMQCon_consume.py

    Arguments:

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


class Consume(object):

    """Class:  Consume

    Description:  Class stub holder for pika class.

    Methods:
        __init__ -> Class initialization.
        queue_unbind -> Stub holder for queue_unbind function.

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
            func_call -> Arg stub holder.
            queue_name -> Arg stub holder.
            no_ack -> Arg stub holder.

        """

        self.func_call = func_call
        self.queue_name = queue_name
        self.no_ack = no_ack

        return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_queue_arg -> Test with queue argument.
        test_consume -> Test consume method.

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
    def test_queue_arg(self, mock_pika):

        """Function:  test_queue_arg

        Description:  Test with queue argument.

        Arguments:

        """

        mock_pika.PlainCredentials.return_value = "PlainCredentials"
        mock_pika.ConnectionParameters.return_value = "ConnectionParameters"
        mock_pika.BasicProperties.return_value = True
        rmq = rabbitmq_class.RabbitMQCon(self.name, "xxxxx")
        rmq.channel = Consume()

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
        rmq.channel = Consume()

        self.assertTrue(rmq.consume("func_call"))


if __name__ == "__main__":
    unittest.main()
