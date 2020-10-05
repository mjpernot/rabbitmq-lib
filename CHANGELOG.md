# Changelog
All notable changes to this project will be documented in this file.

The format is based on "Keep a Changelog".  This project adheres to Semantic Versioning.


## [2.0.0] - 2020-10-05
Breaking Change.

### Changed
- RabbitMQCon.\_\_init\_\_:  Changed positional arguments to keyword arguments.
- RabbitMQPub.\_\_init\_\_:  Changed positional arguments to keyword arguments.
- create_rmqcon:  Changed configuration argument.
- create_rmqpub:  Changed configuration argument.


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
- RabbitMQ.connect - Set the handler to the self.connection attribute.
- RabbitMQPub.open_channel - Set the handler to the self.channel attribute.
- RabbitMQPub.close_channel - Removed returning channel to calling function.
- RabbitMQPub.bind_queue - Corrected misnamed argument to class call.
- RabbitMQPub.publish_msg - Corrected misnamed argument to class call.
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
