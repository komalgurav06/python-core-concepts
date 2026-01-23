import time

wait_time = 1
max_reries = 5
attempt = 0

while attempt < max_reries:
    print(f"Attempt {attempt + 1} - wait time {wait_time}")
    time.sleep(wait_time)
    wait_time *= 2
    attempt += 1