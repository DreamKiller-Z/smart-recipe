import bluetooth

def receiveMessages():
  server_sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
  
  port = 1
  server_sock.bind(("B8:27:EB:10:0F:FE",port))
  server_sock.listen(1)
  
  client_sock,address = server_sock.accept()
  print( "Accepted connection from " + str(address))
  
  data = client_sock.recv(1024)
  print( "received [%s]" % data)
  
  client_sock.close()
  server_sock.close()


receiveMessages()