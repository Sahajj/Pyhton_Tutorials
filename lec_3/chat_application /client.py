import socket 
port = 3000 
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # creates a socket object
CHUNK =  65535   
# insted of explicitily binding the socket, i will let OS do it 
#  ephemeral ports 
# OS will bind this for us 
hostname = '127.0.0.1' 
while True:
    s.connect((hostname, port))
    message = input("type message: ")
    data = message.encode('ascii')
    s.send(data)
    # data recieved 
    data = s.recv(CHUNK)
    text = data.decode('ascii')
    print(f"Sahaj says {text} ")