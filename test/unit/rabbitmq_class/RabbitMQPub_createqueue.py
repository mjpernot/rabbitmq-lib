#!/usr/bin/python
# Classification (U)

"""Program:  RabbitMQPub_createqueue.py

    Description:  Unit test of RabbitMQPub.create_queue in rabbitmq_class.py.

    Usage:
        test/unit/rabbitmq_class/RabbitMQPub_createqueue.py

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


class CreateQueue(object):

    """Class:  CreateQueue

    Description:  Class stub holder for pika class.

    Methods:
        queue_declare -> Stub holder for queue_declare function.

    """

    def queue_declare(self, queue, durable, auto_delete):

        """Function:  queue_declare

        Description:  Stub holder for queue_declare function.

        Arguments:
            queue -> Arg stub holder.
            durable -> Arg stub holder.
            auto_delete -> Arg stub holder.

        """

        return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_create_queue -> Test create_queue method.

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
    def test_create_queue(self, mock_pika):

        """Function:  test_create_queue

        Description:  Test create_queue method.

        Arguments:

        """

        mock_pika.PlainCredentials.return_value = "PlainCredentials"
        mock_pika.ConnectionParameters.return_value = "ConnectionParameters"
        rq = rabbitmq_class.RabbitMQPub(self.name, "pwd")
        rq.channel = CreateQueue()

        self.assertFalse(rq.create_queue())


if __name__ == "__main__":
    unittest.main()
