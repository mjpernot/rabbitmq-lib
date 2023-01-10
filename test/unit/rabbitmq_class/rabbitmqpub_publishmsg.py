# Classification (U)

"""Program:  rabbitmqpub_publishmsg.py

    Description:  Unit test of rabbitmqpub.publish_msg in rabbitmq_class.py.

    Usage:
        test/unit/rabbitmq_class/rabbitmqpub_publishmsg.py

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


class PublishMsg(object):

    """Class:  PublishMsg

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

        self.exchange = None
        self.routing_key = None
        self.body = None
        self.mandatory = None
        self.properties = None

    def basic_publish(self, exchange, routing_key, body, mandatory,
                      properties):

        """Function:  basic_publish

        Description:  Stub holder for basic_publish function.

        Arguments:
            exchange
            routing_key
            body
            mandatory
            properties

        """

        self.exchange = exchange
        self.routing_key = routing_key
        self.body = body
        self.mandatory = mandatory
        self.properties = properties

        return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_pika_pre
        test_pika_post
        test_publish_msg

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

        Description:  Test with Pika version less than 1.0.0.

        Arguments:

        """

        mock_pika.PlainCredentials.return_value = "PlainCredentials"
        mock_pika.ConnectionParameters.return_value = "ConnectionParameters"
        mock_pika.BasicProperties.return_value = True
        rmq = rabbitmq_class.RabbitMQPub(self.name, "xxxxx")
        rmq.channel = PublishMsg()
        mock_pika.__version__ = "0.11.0"

        self.assertTrue(rmq.publish_msg(self.body))

    @mock.patch("rabbitmq_class.pika")
    def test_pika_post(self, mock_pika):

        """Function:  test_pika_post

        Description:  Test with Pika version greater than 1.0.0.

        Arguments:

        """

        mock_pika.PlainCredentials.return_value = "PlainCredentials"
        mock_pika.ConnectionParameters.return_value = "ConnectionParameters"
        mock_pika.BasicProperties.return_value = True
        rmq = rabbitmq_class.RabbitMQPub(self.name, "xxxxx")
        rmq.channel = PublishMsg()
        mock_pika.__version__ = "1.2.0"

        self.assertTrue(rmq.publish_msg(self.body))

    @mock.patch("rabbitmq_class.pika")
    def test_publish_msg(self, mock_pika):

        """Function:  test_publish_msg

        Description:  Test publish_msg method.

        Arguments:

        """

        mock_pika.PlainCredentials.return_value = "PlainCredentials"
        mock_pika.ConnectionParameters.return_value = "ConnectionParameters"
        mock_pika.BasicProperties.return_value = True
        rmq = rabbitmq_class.RabbitMQPub(self.name, "xxxxx")
        rmq.channel = PublishMsg()
        mock_pika.__version__ = "1.2.0"

        self.assertTrue(rmq.publish_msg(self.body))


if __name__ == "__main__":
    unittest.main()
