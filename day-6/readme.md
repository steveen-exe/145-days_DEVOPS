# Day 6/145 – Linux Networking & Connectivity

> Part of my **145-Day DevOps & Cloud Engineering Challenge** 🚀

## 📅 Day Overview

Today's focus was understanding Linux networking fundamentals and learning how to troubleshoot network-related issues like a DevOps Engineer or Site Reliability Engineer (SRE).

Networking is one of the most important skills for production support, Kubernetes, cloud platforms, and troubleshooting application connectivity.

---

# 🎯 Objectives

- Understand Linux networking basics
- Check IP addresses and routing
- Test network connectivity
- Verify DNS resolution
- Inspect open ports
- Monitor active network connections
- Download resources using Linux utilities

---

# 📚 Topics Covered

- IP Address Management
- Routing Table
- Network Connectivity
- DNS Resolution
- Listening Ports
- Active Connections
- HTTP Requests
- File Downloads
- Network Interfaces

---

# 🛠 Commands Practiced

## 1. View IP Address

```bash
ip addr
```

or

```bash
hostname -I
```

**Production Use Case**

- Verify server IP after deployment.
- Confirm Kubernetes node or VM IP address.

---

## 2. View Routing Table

```bash
ip route
```

**Production Use Case**

- Diagnose internet connectivity issues.
- Verify default gateway configuration.

---

## 3. Test Network Connectivity

```bash
ping google.com
```

```bash
ping 8.8.8.8
```

**Production Use Case**

- Verify external connectivity.
- Differentiate between network and DNS issues.

---

## 4. DNS Lookup

```bash
nslookup google.com
```

or

```bash
dig google.com
```

**Production Use Case**

- Verify DNS resolution.
- Troubleshoot service discovery issues.

---

## 5. Check Listening Ports

```bash
ss -tulnp
```

or

```bash
ss -lnt
```

**Production Use Case**

- Confirm application ports are listening.
- Detect unexpected services running on a server.

---

## 6. View Active Connections

```bash
ss -ant
```

**Production Use Case**

- Monitor active client connections.
- Identify excessive connections during incidents.

---

## 7. Trace Network Route

```bash
traceroute google.com
```

Install if required:

```bash
sudo apt install traceroute
```

**Production Use Case**

- Identify where network traffic is failing.
- Troubleshoot latency across networks.

---

## 8. Make HTTP Requests

```bash
curl https://example.com
```

Headers only:

```bash
curl -I https://example.com
```

**Production Use Case**

- Verify APIs and web services.
- Check HTTP response status.

---

## 9. Download Files

```bash
wget https://example.com/file.zip
```

**Production Use Case**

- Download installation packages.
- Retrieve deployment artifacts.

---

## 10. View Network Interfaces

```bash
ip link
```

**Production Use Case**

- Check interface status.
- Verify NIC availability on Linux servers.

---

# 🧪 Mini Lab

Completed the following exercises:

- [ ] Display IP address
- [ ] Show routing table
- [ ] Ping google.com
- [ ] Ping 8.8.8.8
- [ ] Verify DNS using nslookup
- [ ] List listening ports
- [ ] View HTTP headers using curl
- [ ] Download a sample file using wget
- [ ] Identify the default gateway
- [ ] Document observations

---

# 🚨 Production Scenario

## Problem

A Kubernetes Pod cannot connect to the backend database.

### Investigation Steps

```bash
ping <database-ip>

nslookup <database-host>

ip route

ss -tulnp

curl http://<service>:<port>
```

### Possible Causes

- DNS resolution failure
- Incorrect routing
- Firewall blocking traffic
- Database service not listening
- Kubernetes Service misconfiguration
- Network Policy restrictions

### Resolution

- Verify DNS configuration.
- Confirm routing table.
- Ensure database service is running.
- Validate firewall/security group rules.
- Check Kubernetes Service and Endpoints.

---

# 💡 Key Learnings

- Learned how Linux networking works.
- Understood the difference between IP connectivity and DNS resolution.
- Practiced inspecting ports and active connections.
- Used curl and wget for HTTP communication.
- Learned a structured approach to troubleshooting production network issues.

---

# 📝 Commands Summary

| Command | Purpose |
|----------|---------|
| `ip addr` | Show IP addresses |
| `hostname -I` | Display system IP |
| `ip route` | Show routing table |
| `ping` | Test connectivity |
| `nslookup` | DNS lookup |
| `dig` | Advanced DNS query |
| `ss -tulnp` | View listening ports |
| `ss -ant` | View active TCP connections |
| `traceroute` | Trace packet route |
| `curl` | Send HTTP requests |
| `wget` | Download files |
| `ip link` | Show network interfaces |

---

# 🎯 Skills Gained

- Linux Networking
- DNS Troubleshooting
- HTTP Testing
- Network Diagnostics
- Linux System Administration
- DevOps Troubleshooting
- Production Incident Analysis

---

# 🚀 Next Step

**Day 7 – Linux Process & Service Management**

Topics include:

- Process management
- Background jobs
- System services
- `systemctl`
- `journalctl`
- Process monitoring
- Troubleshooting crashed services

---

## 📌 Progress

- ✅ Day 1 – Linux Basics
- ✅ Day 2 – File Management
- ✅ Day 3 – Text Processing
- ✅ Day 4 – Users & Permissions
- ✅ Day 5 – Process Monitoring
- ✅ **Day 6 – Linux Networking & Connectivity**
- ⏳ Day 7 – Process & Service Management

---

**145 Days | DevOps • Cloud • Kubernetes • SRE • Automation**
```