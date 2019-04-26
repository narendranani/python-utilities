import sys, os, time, _thread

# Keep track of thread PIDs
t1, t2 = 0, 0


# The major thread function
def f(timeslice):
    # Set t2 to the PID for this thread
    global t2
    t2 = os.getpid()
    # Loop, do something after every timeslice
    while True:
        # You would do something intelligent here
        time.sleep(timeslice)


# Set t1 to the PID for the parent thread
t1 = os.getpid()
# Start a new thread
_thread.start_new_thread(f, (10,))
# Wait a bit and print the two PIDs
time.sleep(1)
print("PIDs:", t1, t2)
# Give the user an option to stop the thread and the program
while True:
    answer = input("Stop thread now? Y/N: ")
    if answer in ["Y", "y"]:
        os.popen("kill -9 " + str(t2))
        break
# Do something here - maybe cleanup?
# Terminate gracefully
sys.exit(0)
