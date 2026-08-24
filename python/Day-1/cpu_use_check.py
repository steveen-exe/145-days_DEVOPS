#psutil library
#process and system utilities
#retrive info on running processes and hardward utilization
cpu = int(input("Enter the CPU:"))
print(cpu)
if cpu > 50:
    print("Usage warning")
else: 
    print("CPU usage is normal")