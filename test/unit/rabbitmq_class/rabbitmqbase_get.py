# Classification (U)

"""Program:  rabbitmqbase_get.py

    Description:  Unit testing of RabbitMQBase.get in rabbitmq_class.py.

    Usage:
        test/unit/rabbitmq_class/rabbitmqbase_get.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest
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
        json

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

    def json(self):

        """Function:  json

        Description:  Representation for requests.json method.

        Arguments:

        """

        return {}


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_basic

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.name = "UserName"
        self.japd = "Japd"
        self.requests = Requests()

    @mock.patch("rabbitmq_class.requests.get")
    def test_basic(self, mock_get):

        """Function:  test_basic

        Description:  Test with basic set up.

        Arguments:

        """

        mock_get.return_value = self.requests

        rmq = rabbitmq_class.RabbitMQBase(self.name, self.japd)

        self.assertEqual(rmq.get(), {})


if __name__ == "__main__":
    unittest.main()
