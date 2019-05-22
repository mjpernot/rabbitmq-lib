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

##### Unit:  rabbitmq_class.py
```
test/unit/rabbitmq_class/RabbitMQ_init.py
test/unit/rabbitmq_class/RabbitMQ_connect.py
test/unit/rabbitmq_class/RabbitMQ_close.py
```

##### Unit:  All units
```
test/unit/rabbitmq_class/unit_test_run.sh
```

### Unit test code coverage
```
test/unit/rabbitmq_class/code_coverage.sh
```

