# load additional Python modules
import socket  
import time

# create TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# retrieve local hostname
local_hostname = socket.gethostname()

# get fully qualified hostname
local_fqdn = socket.getfqdn()

# get the according IP address
ip_address = socket.gethostbyname(local_hostname)

# bind the socket to the port 23456, and connect
server_address = (ip_address, 23456)  
sock.connect(server_address)  
print ("connecting to %s (%s) with %s" % (local_hostname, local_fqdn, ip_address))

# define example data to be sent to the server
temperature_data = ["$$u 0ÿ{FF}™U093446.000,A,2740.7448,N,08520.8562,E,0.01,101.81,200219,,,A*6A|0.79|1322.7|0000|0000,0000|000004668,Þ","$$u 0ÿ{FF}™U093446.000,A,2740.7448,N,08520.8562,E,0.01,101.81,200219,,,A*6A|0.79|1322.7|0000|0000,0000|000004668,Þ"]  
for entry in temperature_data:  
    print ("data: %s" % entry)
    new_data = str(entry).encode("utf-8")
    sock.sendall(new_data)
    #sock.sendall(entry)
    # wait for two seconds
    time.sleep(2)

# close connection
sock.close()  
