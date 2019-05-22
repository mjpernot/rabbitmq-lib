#!/usr/bin/python
# Classification (U)

"""Program:  RabbitMQPub_createconnection.py

    Description:  Unit test of RabbitMQPub.create_connection in
        rabbitmq_class.py.

    Usage:
        test/unit/rabbitmq_class/RabbitMQPub_createconnection.py

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


class CreateConnection(object):

    """Class:  CreateConnection

    Description:  Class stub holder for pika class.

    Super-Class:  None

    Sub-Classes:  None

    Methods:
        exchange_declare -> Stub holder for exchange_declare function.

    """

    def __init__(self):

        """Function:  __init__

        Description:  Stub holder for __init__ function.

        Arguments:
            None

        """

        self.is_open = True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Super-Class:  unittest.TestCase

    Sub-Classes:  None

    Methods:
        setUp -> Initialize testing environment.
        test_fail_connect -> Test with failure to connect.

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

    @mock.patch("rabbitmq_class.RabbitMQPub.connect")
    @mock.patch("rabbitmq_class.pika")
    def test_fail_connect(self, mock_pika, mock_connect):

        """Function:  test_fail_connect

        Description:  Test with failure to connect.

        Arguments:
            None

        """

        mock_pika.PlainCredentials.return_value = "PlainCredentials"
        mock_pika.ConnectionParameters.return_value = "ConnectionParameters"
        mock_connect.return_value = (False, "Failed to connect")
        rq = rabbitmq_class.RabbitMQPub(self.name, "pwd")

        self.assertEqual(rq.create_connection(), (False, "Failed to connect"))


if __name__ == "__main__":
    unittest.main()
