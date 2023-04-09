import socket
import datetime

# Define host and port
HOST = '127.0.0.1'
PORT = 12345

# Create socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind socket to a specific address and port
server_socket.bind((HOST, PORT))

# Listen for incoming connections
server_socket.listen()

print(f'Server listening on {HOST}:{PORT}')

# Accept incoming connections
client_socket, address = server_socket.accept()

print(f'Connected by {address}')

# Get the current date and time
now = datetime.datetime.now()

# Send the date and time to the client
client_socket.send(now.strftime('%Y-%m-%d %H:%M:%S').encode())

# Close the socket
client_socket.close()
server_socket.close()

