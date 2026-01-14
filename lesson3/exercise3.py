import time

start_time = time.time()

timeout = 5

print("Entering while loop...")

while time.time() - start_time < 5:
    time.sleep(1)
    time_elapsed = time.time() - start_time
    print(f"Time elapsed: {int(time_elapsed)} secs")
    
total_elapsed = (time.time() - start_time)
print(f"Exited the loop. Total elapsed time: {int(total_elapsed)} secs")