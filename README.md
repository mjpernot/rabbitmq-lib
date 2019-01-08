# Python project that contains common libraries and classes for RabbitMQ.
# Classification (U)

# Description:
  This project consists of a number of Python files that are common function libraries and classes for connecting to and operating in a RabbitMQ system.  These programs are not standalone programs, but are installed in another project to support those programs.


###  This README file is broken down into the following sections:
 * Features
 * Prerequisites
 * Installation
 * Program Descriptions
 * Testing
   - Unit

# Features:
 * Connect to and send commands to a RabbitMQ system.
 * Publish messages to RabbitMQ system.
 * Consume messages from RabbitMQ system.

# Prerequisites:

  * List of Linux packages that need to be installed on the server.
    - python-libs
    - python-devel
    - git
    - python-pip

  * Local class/library dependencies within the program structure.


# Installation:

To install the class to support a program - use the pip installation procedures.
  * Add to requirements-rabbitmq-lib.txt:
      git+ssh://git@sc.appdev.proj.coe.ic.gov/JAC-DSXD/rabbitmq-lib.git#egg=rabbitmq-lib

```
vim requirements-rabbitmq-lib.txt
```

Place the requirements-rabbitmq-lib.txt file in the program's project.
  * Add to program's README.md installation section:
      pip install -r requirements-rabbitmq-lib.txt --target rabbit_lib --trusted-host pypi.appdev.proj.coe.ic.gov
```
vim {PROGRAMS_PROJECT}/README.md
```

Add the system module libraries of requirements.txt to the program's requirements.txt.
  *  If the system modules are already in the {PROGRAMS_PROJECT}/requirements.txt file, then skip step.
```
cat requirements.txt >> {PROGRAMS_PROJECT}/requirements.txt
```

# Program Descriptions:
### Program: rabbitmq_class.py
##### Description: Class definitions and methods for connecting to RabbitMQ system.
##### Classes:
  RabbitMQ => Class which is a representation of a RabbitMQ message system.  A RabbitMQ object is used as proxy to implement the connecting to and closing connection to a RabbitMQ node.


  RabbitMQPub => Class which is a representation of a RabbitMQ Publisher.  A RabbitMQPub object is used as proxy to implement the publishing a message to a RabbitMQ queue.


  RabbitMQCon => Class which is a representation of a RabbitMQ Consumer.  A RabbitMQPub object is used as proxy to implement consuming a message from a RabbitMQ queue.


# Testing

# Unit Testing:

### Description: Testing consists of unit testing for the functions in the rabbitmq_class class.

### Installation:

Install the project using git.
  * Replace **{Python_Project}** with the baseline path of the python program.
  * Replace **{Branch_Name}** with the name of the Git branch being tested.  See Git Merge Request.

```
umask 022
cd {Python_Project}
git clone --branch {Branch_Name} git@sc.appdev.proj.coe.ic.gov:JAC-DSXD/rabbitmq-lib.git
```

Install/upgrade system modules.
```
cd rabbitmq-lib
sudo bash
umask 022
pip install -r requirements.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
exit
```

### Configuration:
  * Please note that the integration testing will require access to a rabbitmq system to run the tests.

Create RabbitMQ configuration files.
```
cd test/unit/rabbitmq_class/config
cp rabbitmq.py.TEMPLATE rabbitmq.py
```

Make the appropriate changes to the RabbitMQ environment.
  * Change these entries in the rabbitmq.py file.  The "user", "passwd", and "host" variables are the connection information to a RabbitMQ node.
    - user = "USER"
    - passwd = "PASSWORD"
    - host = "HOSTNAME"

```
vim rabbitmq.py
chmod 600 rabbitmq.py
```

# Unit test runs for rabbitmq_class.py:
  * Replace **{Python_Project}** with the baseline path of the python program.

```
cd {Python_Project}/rabbitmq-lib
```

### Class:  RabbitMQ
##### Unit:  RabbitMQ.__init__
```
test/unit/rabbitmq_class/test_rabbitmq_init.py
```

##### Unit:  RabbitMQ.connect
```
test/unit/rabbitmq_class/test_rabbitmq_connect.py
```

##### Unit:  RabbitMQ.close
```
test/unit/rabbitmq_class/test_rabbitmq_close.py
```

##### Unit:  All units
```
test/unit/rabbitmq_class/unit_test_run_rabbitmq.sh
```


### Class:  RabbitMQPub
##### Unit:  RabbitMQPub.__init__
```
test/unit/rabbitmq_class/test_rabbitmqpub_init.py
```

##### Unit:  RabbitMQPub.connect
```
test/unit/rabbitmq_class/test_rabbitmqpub_connect.py
```

##### Unit:  RabbitMQPub.open_channel
```
test/unit/rabbitmq_class/test_rabbitmqpub_open_channel.py
```

##### Unit:  RabbitMQPub.setup_exchange
```
test/unit/rabbitmq_class/test_rabbitmqpub_setup_exchange.py
```

##### Unit:  RabbitMQPub.create_queue
```
test/unit/rabbitmq_class/test_rabbitmqpub_create_queue.py
```

##### Unit:  RabbitMQPub.bind_queue
```
test/unit/rabbitmq_class/test_rabbitmqpub_bind_queue.py
```

##### Unit:  RabbitMQPub.check_confirm
```
test/unit/rabbitmq_class/test_rabbitmqpub_check_confirm.py
```

##### Unit:  RabbitMQPub.unbind_queue
```
test/unit/rabbitmq_class/test_rabbitmqpub_unbind_queue.py
```

##### Unit:  RabbitMQPub.drop_queue
```
test/unit/rabbitmq_class/test_rabbitmqpub_drop_queue.py
```

##### Unit:  RabbitMQPub.drop_exchange
```
test/unit/rabbitmq_class/test_rabbitmqpub_drop_exchange.py
```

##### Unit:  RabbitMQPub.close_channel
```
test/unit/rabbitmq_class/test_rabbitmqpub_close_channel.py
```

##### Unit:  RabbitMQPub.close
```
test/unit/rabbitmq_class/test_rabbitmqpub_close.py
```

##### Unit:  RabbitMQPub.create_connection
```
test/unit/rabbitmq_class/test_rabbitmqpub_create_connection.py
```

##### Unit:  RabbitMQPub.drop_connection
```
test/unit/rabbitmq_class/test_rabbitmqpub_drop_connection.py
```

##### Unit:  RabbitMQPub.publish_msg
```
test/unit/rabbitmq_class/test_rabbitmqpub_publish_msg.py
```

##### Unit:  RabbitMQPub.clear_queue
```
test/unit/rabbitmq_class/test_rabbitmqpub_clear_queue.py
```

##### Unit:  RabbitMQPub.setup_queue
```
test/unit/rabbitmq_class/test_rabbitmqpub_setup_queue.py
```

##### Unit:  RabbitMQPub.drop_queue (with if_empty = False)
```
test/unit/rabbitmq_class/test_rabbitmqpub_drop_queue2.py
```

##### Unit:  RabbitMQPub.drop_exchange (with if_unused = False)
```
test/unit/rabbitmq_class/test_rabbitmqpub_drop_exchange2.py
```

##### Post-Testing Cleanup:
  * After testing has been completed, run the cleanup program to remove any test exchanges and queues.

```
test/unit/rabbitmq_class/rabbitmqpub_cleanup.py
```

##### Unit:  All units
  * This program will run all unit tests in a single run and also cleanup the exchange and queues.

```
test/unit/rabbitmq_class/unit_test_run_rabbitmqpub.sh
```


### Class:  RabbitMQCon
##### Unit:  RabbitMQCon.__init__
```
test/unit/rabbitmq_class/test_rabbitmqcon_init.py
```

##### Unit:  RabbitMQCon.consume
```
test/unit/rabbitmq_class/test_rabbitmqcon_consume.py
```

##### Unit:  RabbitMQCon.start_loop
  * This test will require you to press CTRL+C to finish the test.

```
test/unit/rabbitmq_class/test_rabbitmqcon_start_loop.py
```

##### Unit:  RabbitMQCon.ack
```
test/unit/rabbitmq_class/test_rabbitmqcon_ack.py
```

##### Post-Testing Cleanup:
  * After testing has been completed, run the cleanup program to remove any test exchanges and queues.

```
test/unit/rabbitmq_class/rabbitmqcon_cleanup.py
```

##### Unit:  All units
  * This program will run all unit tests in a single run and also cleanup the exchange and queues.

```
test/unit/rabbitmq_class/unit_test_run_rabbitmqcon.sh
```

### Unit all units for all classes
  * This program will run all unit tests for all classes in a single run and also cleanup the exchange and queues.

```
test/unit/rabbitmq_class/unit_test_run.sh
```

### Unit test code coverage
```
test/unit/rabbitmq_class/code_coverage.sh
```

