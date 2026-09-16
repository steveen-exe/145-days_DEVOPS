# create a function that can be reused it shows
# shows the system info
import psutil

cpu = psutil.cpu_percent(interval=1)
memory = psutil.virtual_memory().percent
disk = psutil.disk_usage("/").percent

def getSysdetails():
    systeminfo = {
        "cpu" :cpu,
        "memory" : memory,
        "disk" : disk
    }

