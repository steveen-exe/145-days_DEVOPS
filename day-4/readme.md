# Day 4 - Linux Permissions & Package Management

## 📅 Challenge
**145 Days DevOps Challenge**

Day 4 focuses on understanding Linux file permissions, ownership, package management, and environment variables. These concepts are essential for troubleshooting production servers, securing applications, and managing Linux-based infrastructure.

---

## 📚 Topics Covered

- Linux Users & Groups
- File Permissions
- `chmod`
- `chown`
- Package Management (`apt`)
- Environment Variables
- Directory Tree Visualization

---

## 🛠 Commands Practiced

### User Information

```bash
whoami
id
groups
```

### File Permissions

```bash
ls -l
chmod 755 script.sh
chmod 600 private.txt
chmod 444 readonly.txt
```

### Ownership

```bash
sudo chown <user>:<group> filename
```

### Package Management

```bash
sudo apt update
sudo apt upgrade
sudo apt install tree
sudo apt remove tree
apt search <package>
```

### Environment Variables

```bash
env
export PROJECT="145-days-devops"
echo $PROJECT
```

### Directory Structure

```bash
tree
```

---

## 📂 Lab

Created the following files and directories:

```
.
├── private.txt
├── readonly.txt
├── script.sh
├── test
├── test1.txt
└── test2.txt
```

---

## 🔐 Permission Summary

| Permission | Meaning | Typical Use |
|------------|---------|-------------|
| 755 | rwxr-xr-x | Executable scripts |
| 644 | rw-r--r-- | Regular files |
| 600 | rw------- | Private files, SSH keys |
| 444 | r--r--r-- | Read-only configuration |

---

## 💼 Production Use Cases

- Resolve **Permission Denied** errors.
- Assign correct ownership to application files.
- Install required packages on Linux servers.
- Configure environment variables for applications.
- Verify file access before deployments.

Example:

```bash
ls -l /var/www/html
sudo chown www-data:www-data app.log
chmod 755 deploy.sh
```

---

## 🎯 Key Learnings

- Linux permissions are based on **Owner**, **Group**, and **Others**.
- `chmod` modifies file permissions.
- `chown` changes file ownership.
- `apt` manages software packages on Debian/Ubuntu systems.
- Environment variables store configuration without modifying application code.

---

## 📸 Lab Completion

Successfully completed:

- ✅ File permission management
- ✅ Ownership verification
- ✅ Package installation
- ✅ Environment variable creation
- ✅ Directory structure visualization

---

## 🚀 What's Next

**Day 5 – Linux Processes & Job Control**

Topics:

- ps
- top
- htop
- kill
- killall
- jobs
- bg
- fg
- nice
- nohup

We'll begin debugging Linux processes like a production Support Engineer and DevOps professional.

---

## 📖 Repository

Part of my **145 Days DevOps Challenge** documenting my journey from **Application Support Engineer → DevOps / SRE / Cloud Engineer** through daily hands-on labs and real-world production scenarios.

**#Linux #DevOps #SRE #Cloud #AKS #Kubernetes #LearningInPublic**