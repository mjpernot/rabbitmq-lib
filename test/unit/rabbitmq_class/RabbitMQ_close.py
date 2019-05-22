#!/usr/bin/python
# Classification (U)

"""Program:  RabbitMQ_close.py

    Description:  Unit testing of RabbitMQ.close in rabbitmq_class.py.

    Usage:
        test/unit/rabbitmq_class/RabbitMQ_close.py

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


class PikaClose(object):

    """Class:  FileOpen

    Description:  Class stub holder for file open class.

    Super-Class:  None

    Sub-Classes:  None

    Methods:
        close -> Stub holder for close function.

    """

    def close(self):

        """Function:  close

        Description:  Stub holder for close function.

        Arguments:
            None

        """

        return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Super-Class:  unittest.TestCase

    Sub-Classes:  None

    Methods:
        setUp -> Initialize testing environment.
        test_close -> Test close method.

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

    @mock.patch("rabbitmq_class.pika")
    def test_default(self, mock_pika):

        """Function:  test_default

        Description:  Test __init__ method with default arguments.

        Arguments:
            None

        """

        mock_pika.PlainCredentials.return_value = "PlainCredentials"
        mock_pika.ConnectionParameters.return_value = "ConnectionParameters"
        rq = rabbitmq_class.RabbitMQ(self.name, "pwd")
        rq.connection = PikaClose()

        self.assertFalse(rq.close())


if __name__ == "__main__":
    unittest.main()
