# Classification (U)

"""Program:  rabbitmqbase_init.py

    Description:  Unit testing of RabbitMQBase.__init__ in rabbitmq_class.py.

    Usage:
        test/unit/rabbitmq_class/rabbitmqbase_init.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest

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
        test_default_scheme
        test_default_host
        test_default_port
        test_url
        test_auth
        test_basic

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.name = "UserName"
        self.japd = "Japd"
        self.host = "ServerName"
        self.host2 = "localhost"
        self.port = 15555
        self.port2 = 15672
        self.scheme = "http"
        self.scheme2 = "https"
        self.url = self.scheme + "://" + self.host + ":" + str(self.port)

    def test_default_scheme(self):

        """Function:  test_default_scheme

        Description:  Test with default scheme value.

        Arguments:

        """

        rmq = rabbitmq_class.RabbitMQBase(self.name, self.japd)

        self.assertEqual(rmq.scheme, self.scheme2)

    def test_default_host(self):

        """Function:  test_default_host

        Description:  Test with default host value.

        Arguments:

        """

        rmq = rabbitmq_class.RabbitMQBase(
            self.name, self.japd, scheme=self.scheme)

        self.assertEqual(rmq.host, self.host2)

    def test_default_port(self):

        """Function:  test_default_port

        Description:  Test with default port value.

        Arguments:

        """

        rmq = rabbitmq_class.RabbitMQBase(
            self.name, self.japd, host=self.host, scheme=self.scheme)

        self.assertEqual(rmq.port, self.port2)

    def test_url(self):

        """Function:  test_url

        Description:  Test with url attribute.

        Arguments:

        """

        rmq = rabbitmq_class.RabbitMQBase(
            self.name, self.japd, host=self.host, port=self.port,
            scheme=self.scheme)

        self.assertEqual(rmq.url, self.url)

    def test_auth(self):

        """Function:  test_auth

        Description:  Test with auth attribute.

        Arguments:

        """

        rmq = rabbitmq_class.RabbitMQBase(
            self.name, self.japd, host=self.host, port=self.port,
            scheme=self.scheme)

        self.assertEqual(rmq.auth, (self.name, self.japd))

    def test_basic(self):

        """Function:  test_basic

        Description:  Test with basic attributes.

        Arguments:

        """

        rmq = rabbitmq_class.RabbitMQBase(
            self.name, self.japd, host=self.host, port=self.port,
            scheme=self.scheme)

        self.assertEqual((rmq.name, rmq.host, rmq.port),
                         (self.name, self.host, self.port))


if __name__ == "__main__":
    unittest.main()
