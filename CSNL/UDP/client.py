import socket

def send_file(file_name, udp_socket, server_address):
    try:
        with open(file_name, 'rb') as file:
            data = file.read(1024)
            while data:
                udp_socket.sendto(data, server_address)
                data = file.read(1024)
            # Send an empty data to indicate the end of the file
            udp_socket.sendto(b'', server_address)
    except Exception as e:
        print(f"Error: {e}")

def main():
    server_host = '127.0.0.1'  # Change this to the server's IP address
    server_port = 12345  # Change this to the server's port
    server_address = (server_host, server_port)

    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    file_name = "abc.txt"  # Change this to the file you want to send

    udp_socket.sendto(file_name.encode('utf-8'), server_address)
    send_file(file_name, udp_socket, server_address)
    print(f"File {file_name} sent successfully")

if __name__ == '__main__':
    main()
