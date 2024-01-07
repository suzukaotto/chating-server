import socket
import threading

SERVER = '127.0.0.1'
PORT = 55555

username = input("Enter your username: ")

def send_messages():
    while True:
        message = input()
        client.send(message.encode('utf-8'))
        if message == 'quit':
            break

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))

client.send(username.encode('utf-8'))

send_thread = threading.Thread(target=send_messages)
send_thread.start()

while True:
    try:
        message = client.recv(1024).decode('utf-8')
        print(message)
    except OSError:
        break

client.close()
