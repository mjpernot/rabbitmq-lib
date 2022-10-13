# Classification (U)

"""Program:  rabbitmqbase_put.py

    Description:  Unit testing of RabbitMQBase.put in rabbitmq_class.py.

    Usage:
        test/unit/rabbitmq_class/rabbitmqbase_put.py

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


class Requests(object):

    """Class:  UnitTest

    Description:  Class which is a representation for requests module.

    Methods:
        __init__
        raise_for_status

    """

    def __init__(self):

        """Function:  __init__

        Description:  Initialization for class.

        Arguments:

        """

        pass

    def raise_for_status(self):

        """Function:  raise_for_status

        Description:  Representation for requests.raise_for_status method.

        Arguments:

        """

        return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_data
        test_basic

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.name = "UserName"
        self.japd = "Japd"
        self.data = {"key": "value"}
        self.requests = Requests()

    @mock.patch("rabbitmq_class.requests.put")
    def test_data(self, mock_put):

        """Function:  test_data

        Description:  Test with data passed in.

        Arguments:

        """

        mock_put.return_value = self.requests

        rmq = rabbitmq_class.RabbitMQBase(self.name, self.japd)

        self.assertFalse(rmq.put(data=self.data))

    @mock.patch("rabbitmq_class.requests.put")
    def test_basic(self, mock_put):

        """Function:  test_basic

        Description:  Test with basic set up.

        Arguments:

        """

        mock_put.return_value = self.requests

        rmq = rabbitmq_class.RabbitMQBase(self.name, self.japd)

        self.assertFalse(rmq.put())


if __name__ == "__main__":
    unittest.main()
