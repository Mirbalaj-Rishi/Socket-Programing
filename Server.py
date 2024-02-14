#server
#https://www.youtube.com/watch?v=JNzfG7XMYSg
#https://www.geeksforgeeks.org/socket-programming-python/
print("This is the Server")
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#creates a socket s
port = 6060 # this reserves the port for the program
s.bind((socket.gethostname(), 6060)) #6060 is the port number
s.listen(5) #listen for connection


while True:  # while true used to keep the port open 
    clientSocket, address = s.accept()   #socket the client connects to
    print(f"Connection esatblsihed from address {address}")
    clientSocket.send(bytes("Welcome to the server!!!", "utf-8")) #sends this message to the cleint with utf-8 encoding
    clientSocket.close() 
