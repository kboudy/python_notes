import logging
import sys

"""
DEBUG	Detailed information, typically of interest only when diagnosing problems.
INFO	Confirmation that things are working as expected.
WARNING	An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.
ERROR	Due to a more serious problem, the software has not been able to perform some function.
CRITICAL	A serious error, indicating that the program itself may be unable to continue running.
"""

logging.basicConfig(level=logging.WARNING)
# to log to file:
# logging.basicConfig(filename="logfile.log", level=logging.WARNING)


logging.info("some info that won't be displayed because the logging level is WARNING")
logging.warning("a warning")

try:
    a + b
except Exception as e:
    print(sys.exc_info()[0])  # the error class (<class 'NameError'>)
    print(sys.exc_info()[1])  # the error message (name 'a' is not defined)
    print(sys.exc_info()[2].tb_lineno)  # the line number
