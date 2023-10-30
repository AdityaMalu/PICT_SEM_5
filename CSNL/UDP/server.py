import socket
import os

def receive_file(file_name, udp_socket):
    try:
        with open(file_name, 'wb') as file:
            while True:
                data, addr = udp_socket.recvfrom(1024)
                if not data:
                    break
                file.write(data)
    except Exception as e:
        print(f"Error: {e}")

def main():
    host = '0.0.0.0' 
    port = 12345  

    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind((host, port))

    print(f"UDP server listening on {host}:{port}")

    while True:
        file_name, addr = udp_socket.recvfrom(1024)
        file_name = file_name.decode('utf-8')
        print(f"Receiving file: {file_name}")
        receive_file(file_name, udp_socket)
        print(f"Received {file_name}")

if __name__ == '__main__':
    main()
