import socket
import json
import threading
from datetime import datetime

HOST = '127.0.0.1'
PORT = 8000

def listen_for_data():
    # Start the TCP socket server to listen for incoming data from IoT devices
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)
    print(f"Server listening on {HOST}:{PORT}")

    while True:
        client_socket, addr = server.accept()
        print(f"Connection established with {addr}")
        threading.Thread(target=handle_client, args=(client_socket, addr)).start()

def handle_client(client_socket, addr):
    try:
        while True:
            data = client_socket.recv(1024)
            if not data:
                print(f"Client {addr} disconnected.")
                break
            # Decode and load the data as JSON
            message = data.decode('utf-8')
            payload = json.loads(message)
            timestamp = datetime.now().isoformat()
            print(f"[{timestamp}] Received data from {addr}: {payload}")
    except Exception as e:
        print(f"Error handling client {addr}: {e}")
    finally:
        client_socket.close()

# Start listening for incoming data in a separate thread
def start_socket_listener():
    listener_thread = threading.Thread(target=listen_for_data)
    listener_thread.daemon = True
    listener_thread.start()