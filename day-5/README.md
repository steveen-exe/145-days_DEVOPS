# Day 5 – Linux Process & System Monitoring

> Part of my **145-Day DevOps & SRE Challenge**

## 🎯 Objective

Learn how Linux manages running applications (processes) and how to monitor and troubleshoot system resources such as CPU, memory, and uptime. These are fundamental skills for DevOps, SRE, Cloud Engineers, and Production Support Engineers.

---

# 📚 Topics Covered

- Linux Processes
- Process Monitoring
- Process Management
- Background Jobs
- CPU Monitoring
- Memory Monitoring
- System Information
- Process Tree
- System Uptime
- Production Troubleshooting Basics

---

# 🛠 Commands Practiced

## Process Information

```bash
ps aux
ps -ef
ps aux | grep ssh
ps aux | grep python
ps aux | grep docker
```

Purpose:
- View running processes
- Find Process IDs (PIDs)
- Check CPU and Memory utilization

---

## Real-Time Monitoring

```bash
top
```

Useful Shortcuts

| Key | Function |
|------|----------|
| P | Sort by CPU |
| M | Sort by Memory |
| k | Kill Process |
| q | Quit |

---

## Background Jobs

Start a background process

```bash
sleep 300 &
```

List jobs

```bash
jobs
```

Bring process to foreground

```bash
fg
```

Terminate background job

```bash
kill %1
```

---

## Killing Processes

Find PID

```bash
ps aux | grep sleep
```

Terminate process

```bash
kill <PID>
```

Force terminate

```bash
kill -9 <PID>
```

---

## Process Tree

```bash
pstree
```

Install if missing

```bash
sudo apt install psmisc
```

---

## Memory Usage

```bash
free -h
```

---

## CPU Information

```bash
lscpu
```

---

## Memory Details

```bash
cat /proc/meminfo

vmstat
```

---

## System Uptime

```bash
uptime
```

---

## Hostname

```bash
hostname
```

Temporary hostname change

```bash
sudo hostname test-server
```

---

## Kernel & OS Information

Kernel

```bash
uname -r
```

Complete system information

```bash
uname -a
```

Operating System

```bash
cat /etc/os-release
```

---

# 🧪 Hands-on Lab

Execute the following commands:

```bash
ps aux
ps -ef
top
free -h
uptime
hostname
uname -a
sleep 300 &
jobs
ps aux | grep sleep
kill <PID>
```

---

# 💻 Production Scenarios

## Scenario 1 – High CPU Usage

Symptoms

- Application becomes slow
- Server response time increases

Investigation

```bash
top
```

Locate process

```bash
ps aux | grep node
```

Terminate if required

```bash
kill <PID>
```

---

## Scenario 2 – Airflow Scheduler Hung

```bash
ps aux | grep airflow

top
```

Restart scheduler after identifying the issue.

---

## Scenario 3 – Kubernetes Worker Node Investigation

Check resource utilization

```bash
top
```

Verify kubelet

```bash
ps aux | grep kubelet
```

Verify container runtime

```bash
ps aux | grep containerd
```

---

# 📝 Mini Challenge

Complete the following tasks:

- [ ] Find system uptime
- [ ] Start a background process
- [ ] Find its PID
- [ ] Kill the process
- [ ] Display Top 10 CPU-consuming processes

```bash
ps aux --sort=-%cpu | head -10
```

- [ ] Display Top 10 Memory-consuming processes

```bash
ps aux --sort=-%mem | head -10
```

- [ ] Display kernel version

```bash
uname -r
```

- [ ] Display available RAM

```bash
free -h
```

- [ ] Find SSH process

```bash
ps aux | grep ssh
```

- [ ] Display process tree

```bash
pstree
```

---

# 🎯 Interview Questions

1. What is a Linux process?
2. What is the difference between `ps aux` and `top`?
3. What is a PID?
4. What does `kill -9` do?
5. When should you avoid using `kill -9`?
6. How do you identify a process consuming high CPU?
7. How do you identify a memory leak?
8. What does `uptime` show?
9. What is the difference between `free -h` and `/proc/meminfo`?
10. How would you investigate a slow Kubernetes worker node?

---

# 🚀 Key Takeaways

- Learned to inspect running processes.
- Monitored CPU and memory usage.
- Managed foreground and background jobs.
- Understood how to safely terminate processes.
- Collected system and kernel information.
- Practiced production-style Linux troubleshooting.
- Built foundational skills for DevOps, SRE, and Cloud Operations.

---

# 📅 Progress

✅ Day 5 Completed

**145-Day Progress**

```text
█████□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□

Day 5 / 145
```

---

## 📌 Next Up

**Day 6 – Linux Networking Fundamentals**

Topics include:

- IP Addressing
- Network Interfaces
- `ip` command
- `ss`
- `netstat`
- `ping`
- `traceroute`
- `curl`
- `wget`
- DNS Basics
- Production Network Troubleshooting

---

> *"Every production issue starts with observation. Master Linux process monitoring before automating infrastructure."*
