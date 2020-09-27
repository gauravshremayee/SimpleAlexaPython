#!/usr/bin/python
import os
import subprocess
import signal 
import atexit
import time
print("Excuting demo.py")
proc = subprocess.Popen(["python3", "demo.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

print("wait for child ")
# Here you can get the PID
global child_pid
child_pid = proc.pid

# Now we can wait for the child to complete
#(output, error) = proc.communicate()

#if error:
#    print ("error:", error)

#print ("output:", output)

time.sleep(5)
if child_pid is None:
        pass
else:
        print("Killing Child Process...")
        os.kill(child_pid, signal.SIGTERM)
