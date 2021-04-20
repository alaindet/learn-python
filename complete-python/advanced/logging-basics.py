import logging

# The same instance can be obtained, if using the same logger name
# from different files

# 2021-04-20 01:11:29,494 DEBUG: Debug level (1) log message
# 2021-04-20 01:11:29,494 INFO: Info level (2) log message
# 2021-04-20 01:11:29,494 WARNING: Warning level (3) log message
# 2021-04-20 01:11:29,494 ERROR: Error level (4) log message
# 2021-04-20 01:11:29,494 CRITICAL: Critical level (5) log message
log_format1 = '%(asctime)s %(levelname)s: %(message)s'

# 2021-04-20 01:11:01,450 DEBUG    [logging-basics.py:17] Debug level (1) log message
# 2021-04-20 01:11:01,451 INFO     [logging-basics.py:18] Info level (2) log message
# 2021-04-20 01:11:01,451 WARNING  [logging-basics.py:19] Warning level (3) log message
# 2021-04-20 01:11:01,451 ERROR    [logging-basics.py:20] Error level (4) log message
# 2021-04-20 01:11:01,451 CRITICAL [logging-basics.py:21] Critical level (5) log message
log_format2 = '%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s'

log_date_format = '%Y-%m-%d %H:%M:%S'
log_level=logging.DEBUG
log_file = 'logs.txt'

logging.basicConfig(
    format=log_format2,
    level=log_level,
    filename=log_file,
    datefmt=log_date_format
)

# If the logger is given the module's name, it is scoped for the module
logger = logging.getLogger(__name__)

# If giving custom names to the loggers, any logger which is "child" of a parent
# logger inherits the config. A "child" logger is just a period-separated name
# containing the parent's logger name
#
# Example
# parent_logger = logging.getLogger('books')
# child_logger = logging.getLogger('books.database') # Inherits from 'books' logger

logger.debug('Debug level (1) log message')
logger.info('Info level (2) log message')
logger.warning('Warning level (3) log message')
logger.error('Error level (4) log message')
logger.critical('Critical level (5) log message')

"""
Logging levels are as following (lowest to highest ranking) and can be configured

DEBUG (not shown as default)
INFO (not shown as default)
WARNING
ERROR
CRITICAL
"""
