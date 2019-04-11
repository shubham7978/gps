# load additional Python module
import socket
import pickle
import mysql.connector
'''
cnx= mysql.connector.connect(user='root', password='root', database='rabin')

curA=cnx.cursor(buffered=True)
#urB=cnx.cursor(buffered=True)

query1=("SELECT user_id from logss GROUP BY user_id")
query2=("select id from logss  where user_id = %s order by datee desc limit 5")
#query3=("delete from logss where id not in")
curA.execute(query1)
'''
# create TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# retrieve local hostname
local_hostname = socket.gethostname()

# get fully qualified hostname
local_fqdn = socket.getfqdn()

# get the according IP address
ip_address = socket.gethostbyname(local_hostname)

# output hostname, domain name and IP address
print ("working on %s (%s) with %s" % (local_hostname, local_fqdn, ip_address))

# bind the socket to the port 23456
server_address = (ip_address, 23456)  
print ('starting up on %s port %s' % server_address)  
sock.bind(server_address)

# listen for incoming connections (server mode) with one connection at a time
sock.listen(1)

while True:  
    # wait for a connection
    print ('waiting for a connection')
    connection, client_address = sock.accept()

    try:
        # show who connected to us
        print ('connection from', client_address)
        pickle_out=open("gps.pickle","wb")


        # receive the data in small chunks and print it
        while True:
            data = connection.recv(4096)
            if data:
                # output received data
                #print ("Data: %s" % data)
                strng=(str(data,'utf-8'))
                #unformatted=[]
                unformatted= strng.split('|')
                coords=unformatted[0].split(',')
                lat=float(coords[2])/100
                lon=float(coords[4])/100
                speed=unformatted[1]
                altitude= unformatted[2]

                print("lat:%s \n lon: %s \n speed: %s \n altitude: %s \n" %(lat,lon,speed,altitude))
            else:                # no more data -- quit the loop
                print ("no more data.")

                break
    finally:
        # Clean up the connection
        connection.close()
