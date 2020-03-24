#!/usr/bin/python
# Classification (U)

"""Program:  RabbitMQPub_clearqueue.py

    Description:  Unit test of RabbitMQPub.clear_queue in rabbitmq_class.py.

    Usage:
        test/unit/rabbitmq_class/RabbitMQPub_clearqueue.py

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


class ClearQueue(object):

    """Class:  ClearQueue

    Description:  Class stub holder for pika class.

    Methods:
        queue_purge -> Stub holder for queue_purge function.

    """

    def queue_purge(self, queue):

        """Function:  queue_purge

        Description:  Stub holder for queue_purge function.

        Arguments:
            queue -> Arg stub holder.

        """

        return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_clear_queue -> Test clear_queue method.

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
    def test_clear_queue(self, mock_pika):

        """Function:  test_clear_queue

        Description:  Test clear_queue method.

        Arguments:

        """

        mock_pika.PlainCredentials.return_value = "PlainCredentials"
        mock_pika.ConnectionParameters.return_value = "ConnectionParameters"
        mock_pika.BasicProperties.return_value = True
        rq = rabbitmq_class.RabbitMQPub(self.name, "pwd")
        rq.channel = ClearQueue()

        self.assertFalse(rq.clear_queue())


if __name__ == "__main__":
    unittest.main()
