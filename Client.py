#client
#https://www.youtube.com/watch?v=JNzfG7XMYSg
#https://www.geeksforgeeks.org/socket-programming-python/
print("This is the Client")
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # creats a socket s
s.connect((socket.gethostname(), 6060)) #looks for the socket on port 6060

message = s.recv(2048) # recceives a message of 2048 bytes

print(f"Message receive: {message}")
