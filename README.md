# Python project that contains common libraries and classes for RabbitMQ.
# Classification (U)


# Description:
  This project consists of a number of Python files that are common function libraries and classes for connecting to and operating in a RabbitMQ system.


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
    - git
    - python-pip


# Installation:
  There are two types of installs: pip and git.  Pip will only install the program modules and classes, whereas git will install all modules and classes including testing programs along with README.md and CHANGELOG.md files.  The Pip installation will be modifying another program's project to install these supporting librarues via pip.

### Pip Installation:
  * Replace **{Other_Python_Project}** with the baseline path of another python program.

Create requirements-rabbitmq-lib.txt in another program's project.

```
echo "git+ssh://git@sc.appdev.proj.coe.ic.gov/JAC-DSXD/rabbitmq-lib.git#egg=rabbitmq-lib" >> {Other_Python_Project}/requirements-rabbitmq-lib.txt
```

Place the following command into the another program's README.md file under the "Install supporting classes and libraries" section.
   pip install -r /requirements-rabbitmq-lib.txt --target rabbit_lib --trusted-host pypi.appdev.proj.coe.ic.gov

```
vim {Other_Python_Project}/README.md
```

Add the RabbitMQ library requirements.txt to the another program's requirements.txt file and remove any duplicates.

```
cat requirements.txt >> {PROGRAMS_PROJECT}/requirements.txt
vim {Other_Python_Project}/requirements.txt
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

### Testing:
```
cd {Python_Project}/rabbitmq-lib
test/unit/rabbitmq_class/unit_test_run.sh
```

### Code Coverage:
```
cd {Python_Project}/rabbitmq-lib
test/unit/rabbitmq_class/code_coverage.sh
```

