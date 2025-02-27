import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 666                  # Reserve a port for your service.
print(host, port)
s.bind((host, port))        # Bind to the port
s.listen(5)                 # Now wait for client connection.
while True:
   c, addr = s.accept()     # Establish connection with client.
   print("Got connection from", addr)
   c.send(b"Thank you for connecting")
   c.close()                # Close the connection

print("\n==================================================\n")a