import telnetlib 
import getpass
import sys
# Set the Telnet server address and port number 
host = raw_input("Enter your ip: ")
user = input("Enter your telnet username: ")
password = getpass.getpass() 
  
# Create a Telnet object 
tn = telnetlib.Telnet(host) 
  
# Wait for the login prompt 
tn.read_until("Username: ") 
tn.write(user + "\n") 
if password:
 tn.read_until("Password: ") 
 tn.write(password + "\n")

tn.write("enable\n")
tn.write("cisco\n")
tn.write("sh ip int bri\n")

print (tn.read_all)
