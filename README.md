# Design And Simulation of VLAN for an Enterprise

This repository contains the simulation of VLAN in Cisco Packet Tracer and the implementation of VLAN setup and RIP Routing Protocol simulations in Python 3.

## Report
The case study report can be found [here](https://github.com/vkmanojk/Networks-VirtualLAN/blob/master/Report.pdf)


## Network Simulation
[Click Here](https://github.com/vkmanojk/Networks-VirtualLAN/blob/master/VLAN.pkt) to download the packet tracer file

## RIP Protocol Simulation
[Click Here](https://github.com/vkmanojk/Networks-VirtualLAN/blob/master/RIPv2-Simulation/readme.md) to goto RIP Simulation

# VLAN Simulation
VLAN Simulation is done with the help of Netmiko.
Please find the complete network diagram [here](https://github.com/vkmanojk/Networks-VirtualLAN/blob/master/VLAN.pkt). This file contains the detailed configuration file along with ip address ranges for all the devices. The following is a simulation of a part of the actual setup.
### Simulation Diagram 
![alt text](https://github.com/vkmanojk/Networks-VirtualLAN/blob/master/output/VLanSimulationDiagram.png)

### Netmiko Setup

* apt-get update (If you haven’t done this already.)
* apt-get upgrade
* apt-get install python3-venv
* apt-get install python3-dev
* apt-get install python3-pip
* pip3 install -U netmiko

## How To Use

* python ssh.py
* python vlan.py


## Output And Verification
##### SSH
![alt text](https://github.com/vkmanojk/Networks-VirtualLAN/blob/master/output/sampleoutput1.png)
![alt text](https://github.com/vkmanojk/Networks-VirtualLAN/blob/master/output/sampleoutput2.png)
###
##### VLAN
![alt text](https://github.com/vkmanojk/Networks-VirtualLAN/blob/master/output/sampleoutput3.png)
![alt text](https://github.com/vkmanojk/Networks-VirtualLAN/blob/master/output/sampleoutput4.png)

## Authors
* [Manojkumar V K](https://vkmanojk.github.io/)   [@vkmanojk  ](https://github.com/vkmanojk)    
* [Sudharshan S  ](http://sudharshanshanmugasundaram.github.io/)   [@SudharshanShanmugasundaram](https://github.com/SudharshanShanmugasundaram)    
