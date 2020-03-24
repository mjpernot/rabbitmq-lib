#!/usr/bin/python
# Classification (U)

"""Program:  RabbitMQPub_unbindqueue.py

    Description:  Unit test of RabbitMQPub.unbind_queue in rabbitmq_class.py.

    Usage:
        test/unit/rabbitmq_class/RabbitMQPub_unbindqueue.py

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


class UnbindQueue(object):

    """Class:  UnbindQueue

    Description:  Class stub holder for pika class.

    Methods:
        queue_unbind -> Stub holder for queue_unbind function.

    """

    def queue_unbind(self, queue, exchange, routing_key):

        """Function:  queue_unbind

        Description:  Stub holder for queue_unbind function.

        Arguments:
            queue -> Arg stub holder.
            exchange -> Arg stub holder.
            routing_key -> Arg stub holder.

        """

        return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_unbind_queue -> Test unbind_queue method.

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
    def test_unbind_queue(self, mock_pika):

        """Function:  test_unbind_queue

        Description:  Test unbind_queue method.

        Arguments:

        """

        mock_pika.PlainCredentials.return_value = "PlainCredentials"
        mock_pika.ConnectionParameters.return_value = "ConnectionParameters"
        mock_pika.BasicProperties.return_value = True
        rq = rabbitmq_class.RabbitMQPub(self.name, "pwd")
        rq.channel = UnbindQueue()

        self.assertFalse(rq.unbind_queue())


if __name__ == "__main__":
    unittest.main()
