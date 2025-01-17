# Classification (U)

"""Program:  pub_2_rmq.py

    Description:  Unit testing of pub_2_rmq in rabbitmq_class.py.

    Usage:
        test/unit/rabbitmq_class/pub_2_rmq.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest
import collections
import mock

# Local
sys.path.append(os.getcwd())
import rabbitmq_class                           # pylint:disable=E0401,C0413
import version                                  # pylint:disable=E0401,C0413

__version__ = version.__version__


class RMQTest():

    """Class:  RMQTest

    Description:  Class which is a representation of a RabbitMQ class.

    Methods:
        __init__
        drop_connection
        create_connection
        publish_msg

    """

    def __init__(self):

        """Method:  __init__

        Description:  Initialization instance of the RQTest class.

        Arguments:

        """

        self.exchange = "Test_Exchange"
        self.queue_name = "Test_Queue"
        self.status = collections.namedtuple("RQ", "is_open")
        self.channel = self.status(True)
        self.conn_status = True
        self.err_msg = ""
        self.pub_status = True
        self.msg = None

    def create_connection(self):

        """Method:  create_connection

        Description:  Stub holder for create_connection method.

        Arguments:

        """

        return self.conn_status, self.err_msg

    def drop_connection(self):

        """Method:  drop_connection

        Description:  Stub holder for drop_connection method.

        Arguments:

        """

    def publish_msg(self, msg):

        """Method:  publish_msg

        Description:  Stub holder for publish_msg method.

        Arguments:
            (input) msg

        """

        self.msg = msg

        return self.pub_status


class CfgTest():                                        # pylint:disable=R0903

    """Class:  CfgTest

    Description:  Class which is a representation of a cfg module.

    Methods:
        __init__

    """

    def __init__(self):

        """Method:  __init__

        Description:  Initialization instance of the CfgTest class.

        Arguments:

        """

        self.user = "USERNAME"
        self.pswd = "PSWD"
        self.host = "HOSTNAME"
        self.port = 1111
        self.exchange_name = "EXCHANGE_NAME"
        self.exchange_type = "EXCHANGE_TYPE"
        self.x_durable = True
        self.q_durable = True
        self.auto_delete = True
        self.queue = "QUEUE_NAME"
        self.r_key = "RKEY_NAME"


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_failed_publish
        test_failed_connection
        test_publish_msg

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.cfg = CfgTest()
        self.rmq = RMQTest()
        self.data = "Data to publish"

    @mock.patch("rabbitmq_class.create_rmqpub")
    def test_failed_publish(self, mock_rmq):

        """Function:  test_failed_publish

        Description:  Test with failed publish.

        Arguments:

        """

        self.rmq.pub_status = False
        mock_rmq.return_value = self.rmq

        self.assertEqual(rabbitmq_class.pub_2_rmq(
            self.cfg, self.data), (False, "Failure in publishing to RabbitMQ"))

    @mock.patch("rabbitmq_class.create_rmqpub")
    def test_failed_connection(self, mock_rmq):

        """Function:  test_failed_connection

        Description:  Test with failed connection.

        Arguments:

        """

        self.rmq.conn_status = False
        self.rmq.err_msg = "Failed to connect"
        mock_rmq.return_value = self.rmq

        self.assertEqual(rabbitmq_class.pub_2_rmq(
            self.cfg, self.data), (False, "Failed to connect"))

    @mock.patch("rabbitmq_class.create_rmqpub")
    def test_publish_msg(self, mock_rmq):

        """Function:  test_publish_msg

        Description:  Test publishing message to RabbitMQ.

        Arguments:

        """

        mock_rmq.return_value = self.rmq

        self.assertEqual(rabbitmq_class.pub_2_rmq(
            self.cfg, self.data), (True, None))


if __name__ == "__main__":
    unittest.main()
