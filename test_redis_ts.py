import redis
import time

# Connect to Redis
r = redis.Redis(host='192.168.50.101', port=16379, db=0)

# # Check if the time series already exists
# if not r.exists('myts'):
#     # Create a new time series
#     r.execute_command('TS.CREATE', 'myts')

# # Add multiple data points to the time series
# for i in range(10):
#     timestamp = int(time.time() * 1000)  # current time in milliseconds
#     r.execute_command('TS.ADD', 'myts', timestamp, 50 + i)
#     time.sleep(1)  # wait for 1 second before adding the next data point

# # Retrieve all data points we just added
# result = r.execute_command('TS.RANGE', 'myts', '-', '+')

result = r.execute_command('TS.RANGE', 'is-bitcoin-lit:sentiment:mean:30s', '-', '+')

print(result)
