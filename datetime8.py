import time

input("Press Enter to start stopwatch")
start = time.time()

input("Press Enter to stop stopwatch")
end = time.time()

print("Elapsed Time:", int(end - start), "seconds")