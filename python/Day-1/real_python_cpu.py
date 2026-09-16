import psutil
#This module allows you to spawn processes, connect to their
#input/output/error pipes, and obtain their return codes.

#dir -> tell you everything that we can do with a particular lib.

#print(psutil.cpu_times(interval=1))
print(dir(psutil))

print(psutil.subprocess.__doc__)#

#i need to get the cpu for 5 sec --- again and again
for i in range(5):
    print(psutil.cpu_percent(interval=1))


#take a threshold from the user and cehck the cpu is healthy

thresh = float(input("enter a value: "))
for i in range(5):
    if psutil.cpu_percent(interval=1) > thresh:
        print("Not Healthy")
    







