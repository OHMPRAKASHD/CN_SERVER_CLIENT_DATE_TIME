import socket

# Define host and port
HOST = '127.0.0.1'
PORT = 12345

# Create socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((HOST, PORT))

print('Connected to server')

# Receive date and time from the server
data = client_socket.recv(1024).decode()

# Print the received date and time
print(f'Date and time received from server: {data}')

# Close the socket
client_socket.close()

