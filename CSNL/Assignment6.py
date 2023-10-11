import socket
import threading

# Function to handle client connections
def handle_client(client_socket):
    request = client_socket.recv(1024).decode()
    if request == "hello":
        client_socket.send("Hello from the server!".encode())
    elif request == "file_transfer":
        # Implement file transfer logic here
        pass
    elif request == "calculator_arithmetic":
        # Implement arithmetic calculator logic here
        pass
    elif request == "calculator_trigonometry":
        # Implement trigonometry calculator logic here
        pass
    client_socket.close()

# Create a socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 8888))
server.listen(5)

print("Server listening on port 8888")

while True:
    client, addr = server.accept()
    print(f"Accepted connection from {addr[0]}:{addr[1]}")

    # Create a thread to handle the client request
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()


