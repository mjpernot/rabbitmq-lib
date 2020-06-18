# Python project that contains common libraries and classes for RabbitMQ.
# Classification (U)


# Description:
  This project consists of a number of Python files that are common function libraries and classes for connecting to and operating in a RabbitMQ system.


###  This README file is broken down into the following sections:
 * Prerequisites
 * Installation
 * Testing
   - Unit


# Prerequisites:

  * List of Linux packages that need to be installed on the server.
    - git
    - python-pip


# Installation:
  There are two types of installs: pip and git.

### Pip Installation:
  * Replace **{Other_Python_Project}** with the baseline path of another python program.

###### Create requirements file in another program's project to install rabbitmq-lib as a library module.

Create requirements-rabbitmq-lib.txt file:
```
vim {Other_Python_Project}/requirements-rabbitmq-lib.txt
```

Add the following lines to the requirements-rabbitmq-lib.txt file:
```
git+ssh://git@sc.appdev.proj.coe.ic.gov/JAC-DSXD/rabbitmq-lib.git#egg=rabbitmq-lib
```

##### Modify the other program's README.md file to add the pip commands under the "Install supporting classes and libraries" section.

Modify the README.md file:
```
vim {Other_Python_Project}/README.md
```

Add the following lines under the "Install supporting classes and libraries" section.
```
pip install -r requirements-rabbitmq-lib.txt --target rabbit_lib --trusted-host pypi.appdev.proj.coe.ic.gov
```

##### Add the general Rabbitmq-lib requirements to the other program's requirements.txt file.  Remove any duplicates.

Modify the requirements.txt file:
```
vim {Other_Python_Project}/requirements.txt
```

Add the following lines to the requirements.txt file:
```
pika==0.11.0
```

### Git Installation:

Install general Python libraries and classes using git.
  * Replace **{Python_Project}** with the baseline path of the python program.

```
cd {Python_Project}
git clone git@sc.appdev.proj.coe.ic.gov:JAC-DSXD/rabbitmq-lib.git
```

Install/upgrade system modules.

```
sudo bash
umask 022
pip install -r requirements.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
exit
```


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

