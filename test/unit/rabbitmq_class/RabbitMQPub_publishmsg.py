#!/usr/bin/python
# Classification (U)

"""Program:  RabbitMQPub_publishmsg.py

    Description:  Unit test of RabbitMQPub.publish_msg in rabbitmq_class.py.

    Usage:
        test/unit/rabbitmq_class/RabbitMQPub_publishmsg.py

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


class PublishMsg(object):

    """Class:  PublishMsg

    Description:  Class stub holder for pika class.

    Methods:
        basic_publish -> Stub holder for basic_publish function.

    """

    def basic_publish(self, exchange, routing_key, body, mandatory,
                      properties):

        """Function:  basic_publish

        Description:  Stub holder for basic_publish function.

        Arguments:
            exchange -> Arg stub holder.
            routing_key -> Arg stub holder.
            body -> Arg stub holder.
            mandatory -> Arg stub holder.
            properties -> Arg stub holder.

        """

        return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_publish_msg -> Test publish_msg method.

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
    def test_publish_msg(self, mock_pika):

        """Function:  test_publish_msg

        Description:  Test publish_msg method.

        Arguments:

        """

        mock_pika.PlainCredentials.return_value = "PlainCredentials"
        mock_pika.ConnectionParameters.return_value = "ConnectionParameters"
        mock_pika.BasicProperties.return_value = True
        rq = rabbitmq_class.RabbitMQPub(self.name, "xxxxx")
        rq.channel = PublishMsg()

        self.assertTrue(rq.publish_msg(self.body))


if __name__ == "__main__":
    unittest.main()
