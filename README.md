# Python project that contains common libraries and classes for RabbitMQ.
# Classification (U)


# Description:
  This project consists of a number of Python files that are common function libraries and classes for connecting to and operating in a RabbitMQ system.


###  This README file is broken down into the following sections:
 * Installation
 * Testing
   - Unit


# Installation:
  * From here on out, any reference to **{Python_Project}** or **PYTHON_PROJECT** replace with the baseline path of the python program.
  * Replace any reference to **{Other_Python_Project}** with the baseline path of another python program.
  * There are two types of installs: pip and git.

### Pip Installation:

###### Create requirements file in another program's project to install rabbitmq-lib as a library module.

Create requirements-rabbitmq-lib.txt:

```
cp {Python_Project}/requirements-rabbitmq-lib.txt {Other_Python_Project}/requirements-mysql-lib.txt
```

##### Modify the other program's README.md file to add the pip commands under the "Install supporting classes and libraries" section.

Modify the {Other_Python_Project}/README.md file and add the following line:

Centos 7 (Running Python 2.7):
```
pip install -r requirements-rabbitmq-lib.txt --target rabbit_lib --trusted-host pypi.appdev.proj.coe.ic.gov
```

Redhat 8 (Running Python 3.6):
```
python -m pip install -r requirements-rabbitmq-lib.txt --target rabbit_lib --trusted-host pypi.appdev.proj.coe.ic.gov
```

##### Add the general Rabbitmq-lib requirements to the other program's requirements.txt file.  Remove any duplicates.

Modify the {Other_Python_Project}/requirements.txt file and add the following line:

Centos 7 (Running Python 2.7):
```
enum34==1.1.10
pika==1.2.0
requests==2.22.0
simplejson==2.0.9
six==1.12.0
```

Redhat 8 (Running Python 3.6):
```
enum34==1.1.10
pika==1.2.0
requests==2.22.0
simplejson==3.12.0
six==1.16.0
```

### Git Installation:

Install general Python libraries and classes using git.

```
git clone git@sc.appdev.proj.coe.ic.gov:JAC-DSXD/rabbitmq-lib.git
```

Install/upgrade system modules.

Centos 7 (Running Python 2.7):

```
sudo pip install -r requirements.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
```

Redhat 8 (Running Python 3.6):
NOTE: Install as the user that will run the program.

```
python -m pip install --user -r requirements3.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
```


# Testing

# Unit Testing:

### Installation:

Install the project using the procedures in the GIT Installation section.

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

