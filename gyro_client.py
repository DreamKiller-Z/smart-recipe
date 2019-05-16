# from bluetooth import *

# # Create the client socket
# client_socket=BluetoothSocket( RFCOMM )

# client_socket.connect(("5c:41:5a:44:13:80", 3))

# client_socket.send("Hello World")

# print ("Finished")

# client_socket.close()

import socket
 
HOST = "localhost"
PORT = 8080
 
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))
 
sock.sendall("Hello\n")
data = sock.recv(1024)
print( "1)", data)
 
if ( data == "olleH\n" ):
    sock.sendall("Bye\n")
    data = sock.recv(1024)
    print ("2)", data)
 
    if (data == "eyB}\n"):
        sock.close()
        print ("Socket closed")