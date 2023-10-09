import socket
import threading
import time

# Constants
WINDOW_SIZE = 4
MAX_SEQ_NUM = 7
TIMEOUT = 2  # seconds

# Initialize shared variables
next_seq_num = 0
mutex = threading.Lock()

# Create a socket for communication
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Function to send a packet
def send_packet(seq_num):
    message = f"Packet {seq_num}"
    print(f"Sending packet with sequence number: {seq_num}")
    client_socket.sendto(message.encode('utf-8'), ('127.0.0.1', 12345))

# Function to simulate Go-Back-N sender
def gbn_sender():
    global next_seq_num
    while True:
        mutex.acquire()
        if next_seq_num < MAX_SEQ_NUM:
            # Send packets within the window
            for i in range(next_seq_num, min(next_seq_num + WINDOW_SIZE, MAX_SEQ_NUM + 1)):
                send_packet(i)
                next_seq_num += 1
        mutex.release()
        time.sleep(1)

# Function to receive acknowledgments
def receive_acknowledgment():
    while True:
        ack_data, _ = client_socket.recvfrom(1024)
        seq_num = int(ack_data.decode('utf-8').split()[1])
        print(f"Received ACK for packet with sequence number: {seq_num}")

# Create sender and receiver threads
sender_thread = threading.Thread(target=gbn_sender)
receiver_thread = threading.Thread(target=receive_acknowledgment)

# Start the threads
sender_thread.start()
receiver_thread.start()

# Wait for the threads to finish (you can add a condition to exit)
sender_thread.join()
receiver_thread.join()
