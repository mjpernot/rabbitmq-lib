#!/usr/bin/python
# Classification (U)

"""Program:  RabbitMQCon_consume.py

    Description:  Unit test of RabbitMQCon.consume in rabbitmq_class.py.

    Usage:
        test/unit/rabbitmq_class/RabbitMQCon_consume.py

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


class Consume(object):

    """Class:  Consume

    Description:  Class stub holder for pika class.

    Super-Class:  None

    Sub-Classes:  None

    Methods:
        queue_unbind -> Stub holder for queue_unbind function.

    """

    def basic_consume(self, func_call, queue_name, no_ack):

        """Function:  basic_consume

        Description:  Stub holder for basic_consume function.

        Arguments:
            func_call -> Arg stub holder.
            queue_name -> Arg stub holder.
            no_ack -> Arg stub holder.

        """

        return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Super-Class:  unittest.TestCase

    Sub-Classes:  None

    Methods:
        setUp -> Initialize testing environment.
        test_consume -> Test consume method.

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
        self.body = "Message_Body"

    @mock.patch("rabbitmq_class.pika")
    def test_consume(self, mock_pika):

        """Function:  test_consume

        Description:  Test consume method.

        Arguments:
            None

        """

        mock_pika.PlainCredentials.return_value = "PlainCredentials"
        mock_pika.ConnectionParameters.return_value = "ConnectionParameters"
        mock_pika.BasicProperties.return_value = True
        rq = rabbitmq_class.RabbitMQCon(self.name, "pwd")
        rq.channel = Consume()

        self.assertTrue(rq.consume("func_call"))


if __name__ == "__main__":
    unittest.main()
