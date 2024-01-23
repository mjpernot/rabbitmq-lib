# Classification (U)

"""Program:  setup.py

    Description:  A setuptools based setup module.

"""

# Libraries and Global Variables

# Standard
import os
import setuptools

# Local
import version


# Read in long description from README file.
here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, "README.md")) as f_hdlr:
    LONG_DESCRIPTION = f_hdlr.read()

setuptools.setup(
    name="RabbitMQ_Lib",
    description="RabbitMQ class for publisher and consumer.",
    author="Mark Pernot",
    author_email="Mark.J.Pernot@coe.ic.gov",
    url="https://sc.appdev.proj.coe.ic.gov/JAC-DSXD/rabbitmq-lib",
    version=version.__version__,
    platforms=["Linux"],
    long_description=LONG_DESCRIPTION,

    py_modules=[
        "rabbitmq_class",
        "__init__",
        "version"],

    classifiers=[
        # Common Values:
        #  1 - Pre-Alpha
        #  2 - Alpha
        #  3 - Beta
        #  4 - Field
        #  5 - Production/Stable
        "Development Status :: 5 - Production/Stable",
        "Operating System :: Linux",
        "Operating System :: Linux :: Centos",
        "Operating System :: Linux :: Centos :: 7",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
        "Operating System :: Linux :: RedHat",
        "Operating System :: Linux :: RedHat :: 8",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",        
        "Topic :: Message",
        "Topic :: Message :: RabbitMQ",
        "Topic :: Database :: RabbitMQ :: 3.6.6",
        "Topic :: Database :: RabbitMQ :: 3.8.2"])
