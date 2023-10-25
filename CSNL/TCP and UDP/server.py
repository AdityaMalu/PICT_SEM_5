import socket
import os

# Function to calculate a mathematical expression
def calculate(expression):
    try:
        result = str(eval(expression))
        return result
    except Exception as e:
        return str(e)

# Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 12345)
server_socket.bind(server_address)
server_socket.listen(1)

print("Server is running...")

client_socket, client_address = server_socket.accept()

while True:
    data = client_socket.recv(1024).decode()
    if not data:
        break

    if data.lower() == 'hello':
        response = "Hello from the server!"
        client_socket.send(response.encode())
    elif data.lower() == 'file':
        file_name = client_socket.recv(1024).decode()
        if os.path.exists(file_name):
            with open(file_name, 'rb') as file:
                file_data = file.read()
            client_socket.send(file_data)
        else:
            client_socket.send("File not found".encode())
    else:
        result = calculate(data)
        client_socket.send(result.encode())

client_socket.close()
server_socket.close()
