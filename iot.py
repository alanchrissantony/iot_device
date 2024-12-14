import socket
import random
import string
import json
import threading
from datetime import datetime

# Function to generate random 2-digit numbers
def generate_two_digit_data():
    return str(random.randint(10, 99))

# Function to generate random 3-digit numbers
def generate_three_digit_data():
    return str(random.randint(100, 999))

# Function to generate random 4-digit numbers
def generate_four_digit_data():
    return str(random.randint(1000, 9999))

# Function to generate random 2-letter alphabet
def generate_two_letter_data():
    return ''.join(random.choices(string.ascii_lowercase, k=2))

# Function to generate random 4-letter alphabet
def generate_four_letter_data():
    return ''.join(random.choices(string.ascii_lowercase, k=4))

# Function to send data to the server
def send_data_to_server(data):
    try:
        # Server details
        host = '127.0.0.1'
        port = 8000

        # Create a socket connection
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))

        # Send data to server
        client_socket.sendall(data.encode('utf-8'))

        # Close connection
        client_socket.close()
    except Exception as e:
        print(f"Error sending data: {e}")

# Function to simulate the device sending data
def simulate_device(device_id):
    while True:
        timestamp = datetime.now().isoformat()
        # Generate different types of data
        data_1 = generate_two_digit_data()
        data_2 = generate_three_digit_data()
        data_3 = generate_four_digit_data()
        data_4 = generate_two_letter_data()
        data_5 = generate_four_letter_data()
        data_6 = data_2 + data_4
        data_7 = data_5[:2] + data_3[-2:]  # Swap logic

        # Construct payload to send
        payload = {
            "timestamp": timestamp,
            "device_id": device_id,
            "data": {
                "D1": data_1,
                "D2": data_2,
                "D3": data_3,
                "D4": data_4,
                "D5": data_5,
                "D6": data_6,
                "D7": data_7
            }
        }

        # Convert payload to JSON string
        json_data = json.dumps(payload)

        # Send the data to the server
        send_data_to_server(json_data)

        # Wait before sending the next data
        threading.Event().wait(1)  # send data every second

# Start the simulation
if __name__ == '__main__':
    # Simulate multiple devices
    for device_id in range(1, 6):  # simulate 5 devices
        threading.Thread(target=simulate_device, args=(device_id,)).start()