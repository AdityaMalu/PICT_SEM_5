import socket

# Create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server address and port
server_address = ('localhost', 12345)

# Connect to the server
client_socket.connect(server_address)

while True:
    print("Select an option:")
    print("1. Say Hello")
    print("2. File Transfer")
    print("3. Calculator")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        client_socket.send('hello'.encode())
        response = client_socket.recv(1024).decode()
        print("Server says:", response)
    elif choice == '2':
        client_socket.send('file'.encode())
        file_name = input("Enter the file name: ")
        client_socket.send(file_name.encode())
        file_data = client_socket.recv(1024)
        with open(file_name, 'wb') as file:
            file.write(file_data)
        print(f"File '{file_name}' received.")
    elif choice == '3':
        expression = input("Enter a mathematical expression: ")
        client_socket.send(expression.encode())
        result = client_socket.recv(1024).decode()
        print("Result:", result)
    elif choice == '4':
        break

client_socket.close()
