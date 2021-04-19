import logging

LOGGER_NAME = 'test_logger'

# The same instance can be obtained, if using the same logger name
# from different files
logging.basicConfig(format='%(asctime)s', level=logging.DEBUG)
logger = logging.getLogger(LOGGER_NAME)

logger.info('This will not show up.')
logger.warning('This will.')

"""
Logging levels are as following (lowest to highest ranking) and can be configured

DEBUG (not shown as default)
INFO (not shown as default)
WARNING
ERROR
CRITICAL
"""
