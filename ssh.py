#For use on Devices that need SSH Configured 
import getpass
import telnetlib

#Telnet must first be enabled on the devices
user = input("Enter your telnet username: ")
password = getpass.getpass()

#this can be any file with IP Addresses. In My case its called 
#myswitches 
f = open ('myswitches')


#For each IP address in myswitches do something
for IP in f:
	IP=IP.strip()
	print ("Configuring SSH " + (IP))
	HOST = IP
	tn = telnetlib.Telnet(HOST)

	tn.read_until(b"Username: ")
	tn.write(user.encode('ascii') + b"\n")
	if password:
    	tn.read_until(b"Password: ")
    	tn.write(password.encode('ascii') + b"\n")

#Commands to enable SSH on a Cisco device.
	tn.write(b"conf t\n")
	tn.write(b"ip domain-name nocturnalnetworking.com\n")
	tn.write(b"crypto key gen rsa\n")
	tn.write(b"1024\n")
	tn.write(b"do wr\n")
	tn.write(b"end\n")
	tn.write(b"exit\n")

	print(tn.read_all().decode('ascii'))