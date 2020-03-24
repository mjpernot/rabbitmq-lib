#!/usr/bin/python
# Classification (U)

"""Program:  RabbitMQCon_ack.py

    Description:  Unit test of RabbitMQCon.ack in rabbitmq_class.py.

    Usage:
        test/unit/rabbitmq_class/RabbitMQCon_ack.py

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


class Ack(object):

    """Class:  Ack

    Description:  Class stub holder for pika class.

    Methods:
        queue_unbind -> Stub holder for queue_unbind function.

    """

    def basic_ack(self, delivery_tag):

        """Function:  basic_ack

        Description:  Stub holder for basic_ack function.

        Arguments:
            delivery_tag -> Arg stub holder.

        """

        return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_ack -> Test ack method.

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
        rq = rabbitmq_class.RabbitMQCon(self.name, "pwd")
        rq.channel = Ack()

        self.assertFalse(rq.ack("tag"))


if __name__ == "__main__":
    unittest.main()
