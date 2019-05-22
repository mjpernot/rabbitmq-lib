#!/usr/bin/python
# Classification (U)

"""Program:  RabbitMQPub_createqueue.py

    Description:  Unit test of RabbitMQPub.create_queue in rabbitmq_class.py.

    Usage:
        test/unit/rabbitmq_class/RabbitMQPub_createqueue.py

    Arguments:
        None

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

    Super-Class:  None

    Sub-Classes:  None

    Methods:
        queue_declare -> Stub holder for queue_declare function.

    """

    def queue_declare(self, queue, durable, auto_delete):

        """Function:  channel

        Description:  Stub holder for channel function.

        Arguments:
            queue -> Arg tub holder.
            durable -> Arg tub holder.
            auto_delete -> Arg tub holder.

        """

        return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Super-Class:  unittest.TestCase

    Sub-Classes:  None

    Methods:
        setUp -> Initialize testing environment.
        test_open_channel -> Test open_channel method.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:
            None

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
    def test_open_channel(self, mock_pika):

        """Function:  test_open_channel

        Description:  Test open_channel method.

        Arguments:
            None

        """

        mock_pika.PlainCredentials.return_value = "PlainCredentials"
        mock_pika.ConnectionParameters.return_value = "ConnectionParameters"
        rq = rabbitmq_class.RabbitMQPub(self.name, "pwd")
        rq.channel = CreateQueue()

        self.assertFalse(rq.create_queue())


if __name__ == "__main__":
    unittest.main()
