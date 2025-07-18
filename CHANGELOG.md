# Changelog
All notable changes to this project will be documented in this file.

The format is based on "Keep a Changelog".  This project adheres to Semantic Versioning.


## [2.4.1] - 2025-07-11

### Fixed
- rabbitmq_class.pub_2_rmq: Removed the drop_connection call at the end of the function to prevent trying to close a non-open connection.


## [2.4.0] - 2025-04-29

### Fixed
- rabbitmq_class.pub_2_rmq: Close the connection only if it was opened up.

### Added
- rabbitmq_class.RabbitMQPub.open_channel: Open a channel to a RabbitMQ node.
- rabbitmq_class.RabbitMQPub.close_channel: Close the channel to the RabbitMQ node.

### Changed
- rabbitmq_class.pub_2_rmq: Changed err_msg for failed publishing to UnroutableError.

### Deprecated
- Support for RabbitMQ v3.6 and v3.8.


## [2.3.0] - 2025-01-14
- Removed support for Python 2.7.
- Update urllib3==1.26.20
- Added certifi==2024.12.14

### Changed
- RabbitMQBase: put, post, delete, get: Set timeout to 30 seconds for request call.
- Replaced list() with [].
- get_node: Replaced dict() with {}.
- Converted strings to f-strings.
- Documentation changes.


## [2.2.8] - 2024-11-14

### Fixed
- Set chardet==3.0.4 for Python 3.

### Deprecated
- Support for Python 2.7


## [2.2.7] - 2024-10-25
- Updated chardet==4.0.0 for Python 3.
- Updated pika==1.3.1 for Python 3.
- Updated urllib3==1.26.19 for Python 3.
- Updated requests==2.25.0 for Python 3.
- Added idna==2.10 for Python 3.

### Changed
- Updates to requirements3.txt.
- Documentation updates.


## [2.2.6] - 2024-09-27
- Updated simplejson=3.13.2 for Python 3


## [2.2.5] - 2024-08-07
- Updated simplejson==3.13.2
- Updated requests==2.25.0
- Added certifi==2019.11.28
- Added idna==2.10
- Removed email==4.0.3

### Changed
- Updates to requirements.txt.


## [2.2.4] - 2024-07-29
- Set urllib3 to 1.26.19 for Python 2 for security reasons.

### Added
- rabbitmq.py - Template RabbitMQ configuration file.


## [2.2.3] - 2024-02-21
- Updated module requirements for Python.

### Changed
- Set chardet to 3.0.4 for Python 2 and Python 3.
- Set simplejson to 3.12.0 for Python 3.
- Documentation changes.


## [2.2.2] - 2024-01-23
- Updated to work in RedHat 8 environment.

### Changed
- Documentation updates.


## [2.2.1] - 2022-10-13
- Updated to work in Python 3 too

### Changed
- RabbitMQ.connect: Set exception handler return status to local variable.
- Documentation updates.


## [2.2.0] - 2022-04-21
- Added new classes: RabbitMQBase and RabbitMQApi

### Added
- RabbitMQBase class: Representation of RabbitMQ API connection with the GET, PUT, POST, DELETE objects.
- RabbitMQAdmin class:  Class which contains a list of RabbitMQ administration commands.

### Changed
- Documentation updates.


## [2.1.2] - 2021-10-07
### Changed
- RabbitMQCon.consume:  Added version check, due to change in Pika basic_consume parameter list.
- create_rmqcon:  Set default of no_ack to False if not present in config file.


## [2.1.1] - 2021-09-29
### Fixed
- RabbitMQPub.publish_msg:  Added version check, due to change in Pika basic_publish return status.
- create_rmqcon, create_rmqpub:  Added heartbeat and host_list to RabbitMQ instance call.


## [2.1.0] - 2021-09-28
- Update to work with Pika 1.2.0
- Update to work with RabbitMQ 3.8.2
- Handle connecting to multiple node cluster

### Changed
- RabbitMQCon.\_\_init\_\_:  Passed host_list and heartbeat arguments to superclass call.
- RabbitMQ.\_\_init\_\_:  Added host_list parameter to allow connection to multiple RabbitMQ nodes in a cluster.
- RabbitMQ.\_\_init\_\_:  Added heartbeat parameter to allow setting of heartbeat in connection and changed the heartbeat default value from 5 to 60 due to change in Pika 1.2.0.
- Removed unneccessary \*\*kwargs from arguments lists.
- Documentation updates.


## [2.0.0] - 2020-10-05
Breaking Change.

### Changed
- RabbitMQ.\_\_init\_\_:  Added heartbeat argument to pika.ConnectionParameters call.
- RabbitMQPub.\_\_init\_\_, RabbitMQCon.\_\_init\_\_:  Changed positional arguments to keyword arguments.
- create_rmqpub, create_rmqcon:  Changed configuration argument.


## [1.1.2] - 2020-06-10
### Changed
- RabbitMQCon.\_\_init\_\_:  In super call, changed positional arguments to keyword arguments.
- RabbitMQCon.consume:  Added queue argument to allow a specify queue to be monitored.


## [1.1.1] - 2020-05-11
### Changed
- Documentation updates.


## [1.1.0] - 2020-03-24
### Added
- pub_2_rmq:  All in one function to publish to a RabbitMQ queue.
- create_rmqcon:  Function that creates a RabbitMQ Consumer instance.
- create_rmqpub:  Function that creates a RabbitMQ Publisher instance.


## [1.0.2] - 2019-05-22
### Changed
- Refactored unit testing programs to use mock.
- Documentation updates.


## [1.0.1] - 2018-11-02
### Changed
- Documentation updates.


## [1.0.0] - 2018-09-04
- General release.
- Tested in Python 2.7.


## [0.3.1] - 2018-09-03
### Changed
- Documentation updates.


## [0.3.0] - 2018-05-14
- Field release


## [0.2.1] - 2018-02-23
### Added
- Added single-source version control module.


## [0.2.0] - 2017-12-07
- Beta version release


## [0.1.5] - 2017-12-06
### Changed
- Documentation updates.


## [0.1.4] - 2017-12-05
### Changed
- Documentation updates.


## [0.1.3] - 2017-11-30
### Added
- RabbitMQCon.ack - Method to acknowlege message to RabbitMQ.

### Changed
- RabbitMQCon.start_loop - Exception handling on start_consuming loop.
- RabbitMQCon.consume - Return consumer tag from basic_consume call.


## [0.1.2] - 2017-11-29
### Added
- RabbitMQCon - Added RabbitMQ Consumer class.


## [0.1.1] - 2017-11-14
### Changed
- RabbitMQ.connect - Add exception handlers and return status from method.
- RabbitMQPub.create_connection - Add exception handler and return status from method.


## [0.1.0] - 2017-11-09
- Alpha version release.

### Changed
- RabbitMQPub.\_\_init\_\_ - Removed non-used attributes in the class.


## [0.0.5] - 2017-11-08
### Added
- Add check_confirm method to RabbitMQPub class.
- Add drop_queue method to RabbitMQPub class.
- Add clear_queue method to RabbitMQPub class.
- Add unbind_queue method to RabbitMQPub class.
- Add drop_exchange method to RabbitMQPub class.

### Changed
- RabbitMQPub.setup_queue - Added call to check_confirm during queue creation.
- RabbitMQPub.publish_msg - Return a message confirmation delivery status.
- RabbitMQPub.publish_msg - Added properties argument to basic_publish call.
- RabbitMQPub.publish_msg - Added mandatory option to method and function call.


## [0.0.4] - 2017-11-07
### Fixed
- RabbitMQPub.\_\_init\_\_ - Corrected misnamed argument to superclass call.
- RabbitMQPub.open_channel, RabbitMQ.connect - Set the handler to the self.connection attribute.
- RabbitMQPub.close_channel - Removed returning channel to calling function.
- RabbitMQPub.publish_msg, RabbitMQPub.bind_queue - Corrected misnamed argument to class call.
- RabbitMQPub.create_connection - Removed setting attributes on method return.


## [0.0.3] - 2017-11-06
### Fixed
- RabbitMQ.\_\_init\_\_ - Corrected misnamed attributes.


## [0.0.2] - 2017-11-03
### Added
- RabbitMQPub.close_channel method.
- RabbitMQPub.create_queue method.
- RabbitMQPub.setup_exchange method.
- RabbitMQPub.bind_queue method.
- RabbitMQPub.publish_msg method.
- RabbitMQPub.setup_queue method.
- RabbitMQPub.create_connection method.
- RabbitMQPub.drop_connection method.

### Removed
- RabbitMQPub.setup_queue method.


## [0.0.1] - 2017-11-02
### Added
- RabbitMQ class.
- RabbitMQ.\_\_init\_\_ method.
- RabbitMQ.connect method.
- RabbitMQ.close method.
- RabbitMQPub class.
- RabbitMQPub.open_channel method.
- RabbitMQPub.setup_queue method.
