# https://www.youtube.com/watch?v=3QiPPX-KeSc - This is the video I looked at
import socket
import threading # allows threading which allows you to run mutiple pieces of code at the same time

HEADER = 64 # the first message to the server needs to be 64 bytes that tells you how many bytes the next message will be
PORT = 5050
SERVER = "10.0.0.112" #local ip address from ipconfig 
SERVER = socket.gethostbyname(socket.gethostname()) #this allows the program to get your ip address for you
ADDR = (SERVER, PORT) #creates a tuple with the server and the port
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT" #this message will disconect the client 


"""
AF_INET tells what kind of address the computer will use
sock_stream allows us to stream data through the socket 
"""
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server.bind(ADDR) # binds socket to the ADDR tuple 



def handle_client(conn, addr):
    print(f"New Connection {addr} connected")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT) #figures out the length of the message with the header
        if msg_length: #first message is NONE, it comes from connecting this avoids turning that into an integer
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT) #uses message length to alocate message for the header 
        
            if msg == DISCONNECT_MESSAGE: # this disconnects the client from the server to prevent issues disconnecting 
                connected = False

            print(f"{addr}: {msg}")
            """Send to client """
            conn.send("Message received".encode(FORMAT))



def start():
    server.listen() #allows the servver to listen for connections
    print(f"Server is listing from {SERVER}")
    while True:
        conn, addr = server.accept() #this will allow to get the address we are connected and information about the connect
        """This allows us to handle mutiple clients by creating a new thread for each client"""
        thread = threading.Thread(target=handle_client, args=(conn, addr)) 
        thread.start()
        print(f"Active connections {threading.active_count() - 1}") #the start thread counts as a thread so total threads are client threads + start thread

print("Server is starting...")
start()
