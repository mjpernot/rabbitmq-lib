# Python project that contains common libraries and classes for RabbitMQ.
# Classification (U)


# Description:
  This project consists of a number of Python files that are common function libraries and classes for connecting to and operating in a RabbitMQ system.


###  This README file is broken down into the following sections:
 * Configuration
 * Installation
   - Pip Installation
 * Testing
   - Unit


# Configuration
Any program that wants to use this module to connect to mongo, recommend using the rabbitmq-lib.py file as a baseline configuration file for the rabbitmq connection configuration.


# Installation:

### Pip Installation:

###### Create requirements file in another program's project to install rabbitmq-lib as a library module.

  * Create requirements-rabbitmq-lib.txt.  Replace N.N.N with the version of the library needed.

```
echo 'git+ssh://git@sc.appdev.proj.coe.ic.gov/JAC-DSXD/rabbitmq-lib.git@N.N.N#egg=mysql-lib' > requirements-rabbitmq-lib.txt
```

##### Modify the other program's README.md file to add the pip commands under the "Install supporting classes and libraries" section.

Modify the README.md file and add the following lines to install the library modules:

```
python -m pip install -r requirements-rabbitmq-lib.txt --target rabbit_lib --trusted-host pypi.appdev.proj.coe.ic.gov
```

##### Add the general Rabbitmq-lib requirements to (requirements3.txt) to the other program's requirements3.txt file.


# Testing

### Git Installation:

Install general Python libraries and classes using git.

```
git clone git@sc.appdev.proj.coe.ic.gov:JAC-DSXD/rabbitmq-lib.git
```

Install/upgrade system modules.

NOTE: Install as the user that will run the program.

```
python -m pip install --user -r requirements3.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
```

# Unit Testing:

### Installation:

Install the project using the procedures in the GIT Installation section.

### Testing:
```
test/unit/rabbitmq_class/unit_test_run3.sh
test/unit/rabbitmq_class/code_coverage.sh
```

