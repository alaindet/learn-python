from datetime import datetime, timezone, timedelta
import time
import timeit

print('\nLocal time now')
now = datetime.now()
print(now) # OS-based local time

print('\nUTC now')
my_timezone = timezone.utc
now_utc = datetime.now(my_timezone)
print(now_utc) # UTC+0

print('\nTime delta')
tomorrow = now_utc + timedelta(days=1)
print(tomorrow)

print('\nTime string formatting')
# Time format reference
# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
time_format = '%Y-%m-%d %H:%M'
now_utc_formatted = now_utc.strftime(time_format)
print(now_utc_formatted)

# print('\nTime string parsing')
# input_time_format = '%Y-%m-%d'
# output_time_format = time_format
# user_date = input('Enter the date in YYYY-mm-dd format: ')
# parsed_user_date = datetime.strptime(user_date, input_time_format)
# print(parsed_user_date.strftime(output_time_format))

print('\nTracking timings via time package')

def powers(limit):
    return [x**2 for x in range(limit)]

def measure_timing(func):
    start_time = time.time()
    func()
    stop_time = time.time()
    return stop_time - start_time

LIMIT = 1_000_000

func = lambda: powers(LIMIT)
measured_timing = measure_timing(func)
print(measured_timing)

print('\nTracking timings via timeit package')
statement1 = '[x**2 for x in range(5)]'
statement2 = 'list(map(lambda x: x**2, range(5)))'
# timeit evaluates a Python statement many times and returns the total time
print(timeit.timeit(statement1)) # This is ~15% faster
print(timeit.timeit(statement2))
