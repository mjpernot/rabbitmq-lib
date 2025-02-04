# Classification (U)

"""Program:  rabbitmqbase_delete.py

    Description:  Unit testing of RabbitMQBase.delete in rabbitmq_class.py.

    Usage:
        test/unit/rabbitmq_class/rabbitmqbase_delete.py

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
import rabbitmq_class                           # pylint:disable=E0401,C0413
import version                                  # pylint:disable=E0401,C0413

__version__ = version.__version__


class Requests():                                       # pylint:disable=R0903

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

    @mock.patch("rabbitmq_class.requests.delete")
    def test_basic(self, mock_delete):

        """Function:  test_basic

        Description:  Test with basic set up.

        Arguments:

        """

        mock_delete.return_value = self.requests

        rmq = rabbitmq_class.RabbitMQBase(self.name, self.japd)

        self.assertFalse(rmq.delete())


if __name__ == "__main__":
    unittest.main()
