# https://www.youtube.com/watch?v=3QiPPX-KeSc - This is the video I looked at
import socket

HEADER = 64 # the first message to the server needs to be 64 bytes that tells you how many bytes the next message will be
PORT = 5050
SERVER = "10.0.0.112" #local ip address from ipconfig 
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT" #this message will disconect the client 
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #creates the socket
client.connect(ADDR) #connect to the client

def send(msg): 
    message = msg.encode(FORMAT) #turns message into bytes so it can be sent through the socket
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT) #first message sent lets you know how big the next message is
    """This ensures the first message is able to fit in 64 bytes"""
    send_length +=b' ' * (HEADER - len(send_length)) #byte representation of the string 
    client.send(send_length) #first message gives the length of
    client.send(message) #next message 
    """recieve from server"""
    print(client.recv(2048).decode(FORMAT))

input()
send("Hello world!")
