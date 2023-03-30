import socket 
CHUNK = 65535 # revcieve this at most these byter of data at once 

port = 3000 
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # create a socket object 
#  socket.scoket(family, type)
# AF_NET : family of ipv4 ip address
#  SOCK_DGRAM : UPD, SOCK_STREAM: TCP

# some ip address that the server will listen to when message comes 
hostname = '127.0.0.1'  # ip add of local machine, same foor everyone 
# aka home, there is no place like 127.0.0.1 
s.bind((hostname, port)) # bind the socket with this host machine and on port 3000 
print(f"Server is live on  {s.getsockname()}") 


# run this server infinitly till : i stop this manually 

while True:  # infinite loop
    data, clientAdd = s.recvfrom(CHUNK)  # this is listening infinitely so that 
    # if anyone sends data on port 3000 of home it will invoke this line of code and 
    # we will read the data that is being sent to us 
    message = data.decode('ascii') # data by default travels in bytes
    print(f"\nManu at {clientAdd} Says: {message}")
    message_send = input("Reply :")
    data = message_send.encode('ascii') 
    #  send data to the ip that snet me the data.
    s.sendto(data, clientAdd)
