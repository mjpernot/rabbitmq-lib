# Classification (U)

"""Program:  rabbitmq_class.py

    Description:  Class definitions and methods for RabbitMQ system.

    Classes:
        RabbitMQ
            RabbitMQPub
                RabbitMQCon

"""

# Libraries and Global Variables

# Standard

# Third-party
import pika

# Local
import version

__version__ = version.__version__


def pub_2_rmq(cfg, data, **kwargs):

    """Function:  pub_2_rmq

    Description:  All in one function to publish to a RabbitMQ queue.

    Arguments:
        (input) cfg -> Configuration settings module for the program.
        (input) data -> Data document.
        (output) status -> True|False - Success of publishing to RabbitMQ.
        (output) err_msg -> Error message, if any.

    """

    rmq = create_rmqpub(cfg, cfg.queue, cfg.r_key)
    connect_status, err_msg = rmq.create_connection()

    if connect_status and rmq.channel.is_open:
        if rmq.publish_msg(data):
            status = True
            err_msg = None

        else:
            status = False
            err_msg = "Failure in publishing to RabbitMQ"

    else:
        status = False

    rmq.drop_connection()

    return status, err_msg


def create_rmqcon(cfg, q_name, r_key, **kwargs):

    """Function:  create_rmqcon

    Description:  Create a RabbitMQ Consumer instance.

    Arguments:
        (input) cfg -> Configuration settings module for the program.
        (input) q_name -> Queue name in RabbitMQ.
        (input) r_key -> Routing key in RabbitMQ.
        (output) RabbitMQ Consumer instance.

    """

    return RabbitMQCon(
        cfg.user, cfg.pswd, cfg.host, cfg.port,
        exchange_name=cfg.exchange_name, exchange_type=cfg.exchange_type,
        queue_name=q_name, routing_key=r_key, x_durable=cfg.x_durable,
        q_durable=cfg.q_durable, auto_delete=cfg.auto_delete,
        no_ack=cfg.no_ack)


def create_rmqpub(cfg, q_name, r_key, **kwargs):

    """Function:  create_rmqpub

    Description:  Create a RabbitMQ Publisher instance.

    Arguments:
        (input) cfg -> Configuration settings module for the program.
        (input) q_name -> Queue name in RabbitMQ.
        (input) r_key -> Routing key in RabbitMQ.
        (output) RabbitMQ Publisher instance.

    """

    return RabbitMQPub(
        cfg.user, cfg.japd, cfg.host, cfg.port,
        exchange_name=cfg.exchange_name, exchange_type=cfg.exchange_type,
        queue_name=q_name, routing_key=r_key, x_durable=cfg.x_durable,
        q_durable=cfg.q_durable, auto_delete=cfg.auto_delete)


class RabbitMQ(object):

    """Class:  RabbitMQ

    Description:  Class which is a representation of a RabbitMQ message
        system.  A RabbitMQ object is used as proxy to implement the
        connecting to and closing connection to a RabbitMQ node.

    Methods:
        __init__ -> Class instance initilization.
        connect -> Connects the instance to a RabbitMQ node.
        close -> Close connection to the RabbitMQ node.

    """

    def __init__(self, user, passwd, host="localhost", port=5672, **kwargs):

        """Method:  __init__

        Description:  Initialization of an instance of the RabbitMQ class.

        Arguments:
            (input) user -> User login name.
            (input) passwd ->  User password.
            (input) host -> Hostname of RabbitMQ node.
            (input) port -> RabbitMQ port.  Default port is 5672.

        """

        self.name = user
        self.host = host
        self.port = port
        self.connection = None
        self.creds = pika.PlainCredentials(self.name, passwd)
        self.params = pika.ConnectionParameters(host=self.host, port=self.port,
                                                credentials=self.creds)

    def connect(self, **kwargs):

        """Method:  connect

        Description:  Connects the instance to a RabbitMQ node.

        Arguments:
            (output) connect_status -> True|False - Successfully connected.
            (output) err_msg -> Error message if unsuccessful connection.

        """

        err_msg = None
        connect_status = True

        try:
            self.connection = pika.BlockingConnection(self.params)

        except pika.exceptions.ConnectionClosed as err_msg:
            connect_status = False

        except pika.exceptions.ProbableAuthenticationError as err_msg:
            connect_status = False

        except Exception as err_msg:
            connect_status = False

        return connect_status, err_msg

    def close(self, **kwargs):

        """Method:  close

        Description:  Close the connection to the RabbitMQ node.

        Arguments:

        """

        self.connection.close()


class RabbitMQPub(RabbitMQ):

    """Class:  RabbitMQPub

    Description:  Class which is a representation of a RabbitMQ Publisher, to
        include setting up a connection and channel, creating an exchange and
        queue and dropping and clearing these properties.  A RabbitMQPub object
        is used as proxy to implement the publishing a message to a RabbitMQ
        queue.

    Methods:
        __init__ -> Class instance initilization.
        open_channel -> Open a channel to a RabbitMQ node.
        close_channel -> Close the channel to the RabbitMQ node.
        create_queue -> Setup a queue on a RabbitMQ node.
        setup_exchange -> Create an exchange on a RabbitMQ node.
        bind_queue -> Bind a queue to an exchange.
        publish_msg -> Publish a message to a RabbitMQ queue.
        setup_queue -> Initializes the exchange and queue and binds the queue
            to the exchange.
        create_connection -> Create a connection and a channel, followed by the
            initialization of an exchange and queue.
        drop_connection -> Drop channel and connection.
        check_confirm -> Turn on delivery confirmation for channel.
        drop_queue -> Drop queue from the exchange connected to.
        clear_queue -> Remove messages from the current queue.
        unbind_queue -> Unbind a queue from an exchange.
        drop_exchange -> Drop an exchange from the RabbitMQ node.

    """

    def __init__(self, user, passwd, host="localhost", port=5672,
                 exchange_name="", exchange_type="direct", queue_name="",
                 routing_key="", x_durable=True, q_durable=True,
                 auto_delete=False, **kwargs):

        """Method:  __init__

        Description:  Initialization of an instance of the RabbitMQPub class.

        Arguments:
            (input) user -> User login name.
            (input) passwd ->  User password.
            (input) host -> Hostname of RabbitMQ node.
            (input) port -> RabbitMQ port.  Default = 5672.
            (input) exchange_name -> Name of exchange.
            (input) exchange_type -> Types: direct, fanout, headers, and topic.
            (input) queue_name -> Name of the queue to create.
            (input) routing_key -> Name of queue to rout to.
            (input) x_durable -> True|False - Exchange survives reboots.
            (input) q_durable -> True|False - Queue survives reboots.
            (input) auto_delete -> True|False - Auto-delete after consuming.

        """

        super(RabbitMQPub, self).__init__(user, passwd, host, port, **kwargs)

        self.channel = None

        # Queue declaration attributes
        self.queue_name = queue_name
        self.q_durable = q_durable
        self.auto_delete = auto_delete
        self.q_passive = False
        self.routing_key = routing_key

        # Exchange declaration attributes
        self.exchange = exchange_name
        self.exchange_type = exchange_type
        self.x_durable = x_durable
        self.x_passive = False

    def open_channel(self, **kwargs):

        """Method:  open_channel

        Description:  Open a channel to a RabbitMQ node.

        Arguments:

        """

        self.channel = self.connection.channel()

    def close_channel(self, **kwargs):

        """Method:  close_channel

        Description:  Close the channel to the RabbitMQ node.

        Arguments:

        """

        self.channel.close()

    def create_queue(self, **kwargs):

        """Method:  setup_queue

        Description:  Setup a queue on a RabbitMQ node.

        Arguments:

        """

        self.channel.queue_declare(queue=self.queue_name,
                                   durable=self.q_durable,
                                   auto_delete=self.auto_delete)

    def setup_exchange(self, **kwargs):

        """Method:  setup_exchange

        Description:  Create an exchange on a RabbitMQ node.

        Arguments:

        """

        self.channel.exchange_declare(exchange=self.exchange,
                                      exchange_type=self.exchange_type,
                                      durable=self.x_durable)

    def bind_queue(self, **kwargs):

        """Method:  bind_queue

        Description:  Bind a queue to an exchange.

        Arguments:

        """

        self.channel.queue_bind(queue=self.queue_name, exchange=self.exchange,
                                routing_key=self.routing_key)

    def publish_msg(self, body, mandatory=True, **kwargs):

        """Method:  publish_msg

        Description:  Publish a message to a RabbitMQ queue.

        Arguments:
            (input) body -> Message body being published to RabbitMQ.
            (input) mandatory -> True|False - Message is saved to queue.
            (output) True|False -> Message confirmation delivery status.

        """

        return self.channel.basic_publish(
            exchange=self.exchange, routing_key=self.routing_key,
            body=body, mandatory=mandatory,
            properties=pika.BasicProperties(delivery_mode=2))

    def setup_queue(self, **kwargs):

        """Method:  setup_queue

        Description:  Initialize the exchange and queue and bind the queue to
            the exchange.

        Arguments:

        """

        self.setup_exchange()
        self.create_queue()
        self.bind_queue()
        self.check_confirm()

    def create_connection(self, **kwargs):

        """Method:  create_connection

        Description:  Create a connection and a channel, followed by the
            initialization of an exchange and queue.

        Arguments:
            (output) connect_status -> True|False - Successfully connected.
            (output) err_msg -> Error message if unsuccessful.

        """

        connect_status, err_msg = self.connect()

        if connect_status:
            self.open_channel()

            if self.channel.is_open:
                self.setup_queue()

            else:
                connect_status = False
                err_msg = "Error:  Unable to open channel."

        return connect_status, err_msg

    def drop_connection(self, **kwargs):

        """Method:  drop_connection

        Description:  Drop the channel and connection to RabbitMQ.

        Arguments:

        """

        self.close_channel()
        self.close()

    def check_confirm(self, **kwargs):

        """Method:  check_confirm

        Description:  Turn on the check confirmation for the channel.

        Arguments:

        """

        self.channel.confirm_delivery()

    def drop_queue(self, if_unused=True, if_empty=True, **kwargs):

        """Method:  drop_queue

        Description:  Drop the queue from the exchange.

        Arguments:
            (input) if_unused -> True|False - Only drop if unused.
            (input) if_empty -> True|False - Only drop if empty.

        """

        self.channel.queue_delete(queue=self.queue_name, if_unused=if_unused,
                                  if_empty=if_empty)

    def clear_queue(self, **kwargs):

        """Method:  clear_queue

        Description:  Remove messages from queue.

        Arguments:

        """

        self.channel.queue_purge(queue=self.queue_name)

    def unbind_queue(self, **kwargs):

        """Method:  unbind_queue

        Description:  Unbind a queue from an exchange.

        Arguments:

        """

        self.channel.queue_unbind(queue=self.queue_name,
                                  exchange=self.exchange,
                                  routing_key=self.routing_key)

    def drop_exchange(self, if_unused=True, **kwargs):

        """Method:  drop_exchange

        Description:  Drop an exchange from the RabbitMQ node.

        Arguments:
            (input) if_unused -> True|False - Only drop if unused.

        """

        self.channel.exchange_delete(exchange=self.exchange,
                                     if_unused=if_unused)


class RabbitMQCon(RabbitMQPub):

    """Class:  RabbitMQCon

    Description:  Class which is a representation of a RabbitMQ Consumer, to
        include setting upa consumer callback capability and starting a
        loop to look for new messages in a message queue.  A RabbitMQCon object
        is used as proxy to implement the consuming a message from a RabbitMQ
        queue.

    Methods:
        __init__ -> Class instance initilization.
        consume -> Call Basic Consumecallback function for requested queue.
        start_loop -> Start loop checking for new messages in Rabbitmq queue.
        ack -> Send an acknowledge for a specific message tag.

    """

    def __init__(self, user, passwd, host="localhost", port=5672,
                 exchange_name="", exchange_type="direct", queue_name="",
                 routing_key="", x_durable=True, q_durable=True,
                 auto_delete=False, no_ack=False, **kwargs):

        """Method:  __init__

        Description:  Initialization of an instance of the RabbitMQCon class.

        Arguments:
            (input) user -> User login name.
            (input) passwd ->  User password.
            (input) host -> Hostname of RabbitMQ node.
            (input) port -> RabbitMQ port.  Default = 5672.
            (input) exchange_name -> Name of exchange.
            (input) exchange_type -> Exchange type: direct, fanout, headers,
                and topic.
            (input) queue_name -> Name of the queue to create.
            (input) routing_key -> Name of queue to rout to.
            (input) x_durable -> True|False - Exchange survives reboots.
            (input) q_durable -> True|False - Queue survives reboots.
            (input) auto_delete -> True|False - Auto-delete after consuming.
            (input) no_ack -> True|False - Automatic acknowledgement.

        """

        super(RabbitMQCon, self).__init__(
            user, passwd, host, port, exchange_name=exchange_name,
            exchange_type=exchange_type, queue_name=queue_name,
            routing_key=routing_key, x_durable=x_durable, q_durable=q_durable,
            auto_delete=auto_delete, **kwargs)

        self.no_ack = no_ack

    def consume(self, func_call, **kwargs):

        """Method:  consume

        Description:  Call the Basic Consume callback function for the
            requested queue.

        Arguments:
            (input) func_call -> Name of the callback function.
            (input) **kwargs:
                queue -> Name of queue.
            (output) Return consumer tag that is returned from basic_consume.

        """

        queue = kwargs.get("queue", self.queue_name)

        return self.channel.basic_consume(func_call, queue, self.no_ack)

    def start_loop(self, **kwargs):

        """Method:  start_loop

        Description:  Start an indefinite loop on checking for new messages in
            a RabbitMQ queue.

        Arguments:

        """

        try:
            self.channel.start_consuming()

        except KeyboardInterrupt:
            self.channel.stop_consuming()

        self.close()

    def ack(self, tag, **kwargs):

        """Method:  ack

        Description:  Send an acknowledge for a specific message tag.

        Arguments:
            (input) tag -> Message tag number being acknowledged.

        """

        self.channel.basic_ack(delivery_tag=tag)
