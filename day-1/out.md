27-06


In Linux, everything is treated as a file even if it is a normal file, a directory, or even a
 device such as a printer or keyboard.

| Directory  | Purpose                | Real-world Example          |
| ---------- | ---------------------- | --------------------------- |
| `/`        | Root of the filesystem | Everything starts here      |
| `/home`    | User home directories  | `/home/steve`               |
| `/root`    | Root user's home       | Admin account               |
| `/etc`     | Configuration files    | `nginx.conf`, `sshd_config` |
| `/var`     | Variable data          | Logs, databases, caches     |
| `/var/log` | Log files              | `syslog`, application logs  |
| `/tmp`     | Temporary files        | Installers, temp data       |
| `/usr`     | Installed applications | `python`, `git`, `kubectl`  |
| `/opt`     | Optional software      | Custom enterprise apps      |
| `/proc`    | Process/kernel info    | Virtual filesystem          |

- follows the Filesystem Hierarchy Standard (FHS).


**Types of files in the Linux system**

General Files: They are also called ordinary files. It may be an image, video, program, or simple text file. These types of files can be in ASCII or Binary format.
Directory Files: These types of files are a warehouse for other file types. It may be a directory file within a directory (subdirectory).
Device Files: In a Windows like operating system, devices like CD-ROM and hard drives are represented as drive letters like F: G: H, whereas in the Linux system, devices are represented as files. For example, /dev/sda1, /dev/sda2, and so on.

/boot 
-/boot/vmlinkux -> keranal file
-/boot/grub/grub -> config file used in boottime_grub


device files:
/dev/hda -> primary hda
/dev/null -> write not allowed return EOF

etc - used to strore system config files
/etc/hosts : Maps IP addresses to corresponding hostnames.
/etc/hosts.allow : Specifies which hosts are allowed to access services on the local machine.
/etc/hosts.deny : Lists hosts that are denied access to services on the
/etc/passwd : Contains user account information such as usernames and user IDs (passwords are stored in the shadow file).


/usr - A top-level directory in Linux that contains user-space programs, libraries, documentation, and shared data

/proc - These /proc files provide real time system and process information generated dynamically by the Linux kernel.



Log Files
These files record crucial system events, logins, and activity history for monitoring and troubleshooting.

/var/log/lastlog : Stores information about the last login of each user.
/var/log/messages : Contains general system activity and global log messages, though on modern systemd-based systems logging may instead be handled by journald
/var/log/wtmp : Maintains a history of user login and logout sessions.




refer - https://www.geeksforgeeks.org/linux-unix/linux-directory-structure/


10 linux commands that i used today:-

ls
cd
mkdir
pwd
grep
head
tail
journalctl
echo
find


One production use case for each command.

| Command          | Production Use Case                                                                                                                               |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`ls`**         | Verify that application logs, configuration files, deployment artifacts, or backup files exist in the expected directory before troubleshooting.  |
| **`cd`**         | Navigate to application directories such as `/var/log`, `/etc/nginx`, or `/opt/app` while investigating production issues.                        |
| **`mkdir`**      | Create directories for backups, log archives, deployment packages, or temporary troubleshooting data during maintenance.                          |
| **`pwd`**        | Confirm your current working directory before executing commands to avoid modifying or deleting files in the wrong location.                      |
| **`grep`**       | Search application or system logs for keywords like `ERROR`, `Exception`, `Timeout`, or a specific request ID during incident investigation.      |
| **`head`**       | Quickly inspect the first few lines of configuration files or CSV data to verify headers, file format, or configuration settings.                 |
| **`tail`**       | Monitor the latest application logs to identify errors immediately after a deployment or while reproducing an issue (`tail -f` is commonly used). |
| **`journalctl`** | Review systemd service logs to determine why a service failed to start, crashed, or restarted unexpectedly on a Linux server.                     |
| **`echo`**       | Write configuration values, environment variables, or test messages into files while creating scripts or validating shell commands.               |
| **`find`**       | Locate configuration files, log files, certificates, or deployment artifacts anywhere on a server when their exact location is unknown.           |
