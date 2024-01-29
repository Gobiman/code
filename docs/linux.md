
# Linux

#### Change IP Address in RHEL 9 
list all all IPs, show details of NIC, modify NIC with the new IP, then restart the network
```bash
ip -c a
nmcli device show eth1
nmcli con modify eth1 ipv4.addresses 172.16.1.3/16
nmcli con up eth1
```
#### Network configuration files in RHEL
Network files location, details
```bash
ls /etc/NetworkManager/system-connections
cat ethX.nmconnection
```

#### grep
Grep is a command-line utility for searching plain-text data sets for lines that match a regular expression. 

#### Hostname 

```bash
hostnamectl set-hostname newhostname
```

#### Mount 
mount is a command in various operating systems. Before a user can access a file on a Unix-like machine, the file system on the device which contains the file needs to be mounted with the mount command. Frequently mount is used for SD card, USB storage, DVD and other removable storage devices. 



```bash
# List mount-points
findmnt (optional)<device/directory>
```
```
# Unmount
umount <device/directory>
```
