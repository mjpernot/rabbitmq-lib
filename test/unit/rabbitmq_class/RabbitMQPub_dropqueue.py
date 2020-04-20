#!/usr/bin/python
# Classification (U)

"""Program:  RabbitMQPub_dropqueue.py

    Description:  Unit test of RabbitMQPub.drop_queue in rabbitmq_class.py.

    Usage:
        test/unit/rabbitmq_class/RabbitMQPub_dropqueue.py

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


class DropQueue(object):

    """Class:  DropQueue

    Description:  Class stub holder for pika class.

    Methods:
        basic_publish -> Stub holder for basic_publish function.

    """

    def queue_delete(self, queue, if_unused, if_empty):

        """Function:  queue_delete

        Description:  Stub holder for queue_delete function.

        Arguments:
            queue -> Arg stub holder.
            if_unused -> Arg stub holder.
            if_empty -> Arg stub holder.

        """

        return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_drop_queue -> Test drop_queue method.

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
    def test_drop_queue(self, mock_pika):

        """Function:  test_drop_queue

        Description:  Test drop_queue method.

        Arguments:

        """

        mock_pika.PlainCredentials.return_value = "PlainCredentials"
        mock_pika.ConnectionParameters.return_value = "ConnectionParameters"
        mock_pika.BasicProperties.return_value = True
        rq = rabbitmq_class.RabbitMQPub(self.name, "xxxxx")
        rq.channel = DropQueue()

        self.assertFalse(rq.drop_queue())


if __name__ == "__main__":
    unittest.main()
