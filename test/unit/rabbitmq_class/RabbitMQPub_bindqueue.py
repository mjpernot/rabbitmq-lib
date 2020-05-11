#!/usr/bin/python
# Classification (U)

"""Program:  RabbitMQPub_bindqueue.py

    Description:  Unit test of RabbitMQPub.bind_queue in rabbitmq_class.py.

    Usage:
        test/unit/rabbitmq_class/RabbitMQPub_bindqueue.py

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


class BindQueue(object):

    """Class:  BindQueue

    Description:  Class stub holder for pika class.

    Methods:
        exchange_declare -> Stub holder for exchange_declare function.

    """

    def queue_bind(self, queue, exchange, routing_key):

        """Function:  queue_bind

        Description:  Stub holder for queue_bind function.

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
        test_bind_queue -> Test bind_queue method.

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
    def test_bind_queue(self, mock_pika):

        """Function:  test_bind_queue

        Description:  Test bind_queue method.

        Arguments:

        """

        mock_pika.PlainCredentials.return_value = "PlainCredentials"
        mock_pika.ConnectionParameters.return_value = "ConnectionParameters"
        rmq = rabbitmq_class.RabbitMQPub(self.name, "xxxxx")
        rmq.channel = BindQueue()

        self.assertFalse(rmq.bind_queue())


if __name__ == "__main__":
    unittest.main()
