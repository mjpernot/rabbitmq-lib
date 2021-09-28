#!/usr/bin/python
# Classification (U)

"""Program:  create_rmqcon.py

    Description:  Unit testing of create_rmqcon in rabbitmq_class.py.

    Usage:
        test/unit/rabbitmq_class/create_rmqcon.py

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


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_create_instance

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        class CfgTest(object):

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
                self.japd = "japd"
                self.host = "HOSTNAME"
                self.port = 1111
                self.exchange_name = "EXCHANGE_NAME"
                self.exchange_type = "EXCHANGE_TYPE"
                self.x_durable = True
                self.q_durable = True
                self.auto_delete = True
                self.queue = "QUEUE_NAME"
                self.r_key = "RKEY_NAME"
                self.no_ack = False

        self.cfg = CfgTest()

    @mock.patch("rabbitmq_class.RabbitMQCon")
    def test_create_instance(self, mock_rmq):

        """Function:  test_create_instance

        Description:  Test creating RabbitMQ Consumer Instance.

        Arguments:

        """

        mock_rmq.return_value = "RabbitMQ_Instance"

        self.assertEqual(rabbitmq_class.create_rmqcon(
            self.cfg, self.cfg.queue, self.cfg.r_key), "RabbitMQ_Instance")


if __name__ == "__main__":
    unittest.main()
