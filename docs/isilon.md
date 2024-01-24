# isilon (powerscale)

```bash
#list information for all nodes in the cluster
isi_for_array -s isi_hw_status -i
```
```bash
#list nodes serial number:     
isi_for_array -s isi_hw_status -i | grep SerNo
```
```bash
#get the Software ID (SWID) of the cluster
isi license list | grep -i "OneFS license"
```
```bash
#list drives that NOT healthy
isi_for_array 'isi devices drive list|grep -v "HEALTH\|L3\|EMPTY"'|grep Bay
```
```bash
#list drives status for node 30
isi_for_array -n30 'isi devices drive list'
```
```bash
#suspend sled B so disk can be replaced  for node 30
isi_for_array -n30 'isi devices drive suspend --sled=B --force'	
```
```bash
#list drives status for node 22
isi_for_array -n22 'isi devices list'
```
```bash
#version of OneFS
isi version --format=list	
```
```bash
#contact details 
isi cluster contact view	
```
```bash
#view esrs details
isi esrs view
```
```bash
#shutdown cluster\node
isi cluster shutdown --node-lnn=NodeNumber\All 
#OR
isi config 
shutdown
```
```bash
#list IB status
isi_for_array -s 'ibstat|grep State'
```
```bash
#find drive that requires replacement
isi_for_array 'isi device drive list|grep REPLACE'
```
```bash
#list HW of the node
isi_hw_status 
#list HW status for the cluster
isi_for_array isi_hw_status
```
```bash
#Returns the product number of each node
isi_for_array 'isi_hw_status | grep Product'
```
```bash
#Checking usage
isi quota quotas list | grep -i <sharename>
du -Ash <sharename>
```
```bash
#List Authentication provider
isi_for_array -s 'isi auth status'|grep <Domain Name>|cut -c55-|sort|uniq -c
```
```bash
#Enable/Disable synciqjobs
isi sync policies list
isi sync policies <enable\disable> --all
isi sync policies list
```
#### list devices & adding to the cluster

```bash
# Once nodes are labelled & plugged in 
isi devices node list
isi device node add <SERIAL NUMBER> #SR of the nodes are labelled correctly.
#Monitor join process:
isi status -q
```
#### Replace isilon drive

```bash
#Login to the affected Node on which you facing the issue whilere placing drive .
ssh node
```
```bash
#show the unhealthy drive bay
isi_for_array 'isi devices drive list|grep -v "HEALTH\|L3\|EMPTY"'|grep Bay
```
```bash
# Manually suspend the SLED # 
isi devices drive suspend --sled=<affected sled >
```
```bash
# Verify the sled is suspended and drives are unmounted
tail -f /var/log/isi_drive_d.log
```

```bash
# Verify drives Sled / drives are Suspended
isi devices drive list
```

```bash
#Once the drive is replaced and the sled is re-seated, add the Sledback using below command .
isi devices drive add --sled=<affected sled > 
```

```bash
# Check the drive status
isi devices drive list
```

```bash
# if the disk is used\old, should require formatting
isi devices drive format --node-lnn=<Node_Number> --bay=<Bay_Number>
```

```bash
# After issuing upgrade command & not sure if there is any progress activties 
isi upgrade cluster nodes firmware progress list
```

#### /VAR file system was less than 500MB
Reduce message log file to increase /var to >500mb by using newsyslog command which maintain system log files to manageable sizes.

```bash
# newsyslog: Rotated log file /var/log/messages
newsyslog -F /var/log/messages
# then delete big old isi_tardis_d.log.<nn>.gz files
```

#### Change share permissions from Write\Read to Read only 
```bash
ssh
#Check domain users permission to TBM share:
isi smb shares permission view <shareName> --group="DomainName\Domain Users"
##Change TBM smb share to read only for domain users:
isi smb shares permission modify <shareName> --group="DomainName\Domain Users" --permission=read --permission-type=allow
##And check permissions afterwards:
isi smb shares permission view <shareName> --group="DomainName\Domain Users"
```
#### SmartFail  a node
```bash
isi status -q
isi job jobs list
isi devices node smartfail --node-lnn=<Node Name>
isi job jobs list
isi jon jobs view <Job Number>
```

