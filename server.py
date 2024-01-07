import socket
import threading

HOST = '127.0.0.1'
PORT = 55555

def handle_client(client_socket, client_address):
    try:
        print(f"[NEW CONNECTION] {client_address} connected.")

        username = client_socket.recv(1024).decode('utf-8')
        print(f"[{client_address}] Username: {username}")

        connected = True
        while connected:
            message = client_socket.recv(1024).decode('utf-8')
            if message == 'quit':
                print(f"<{username}> Connection has been terminated.")
                connected = False
                break

            print(f"[{username}] {message}")
            for c in clients:
                if c != client_socket:
                    c.send(f"[{username}] {message}".encode('utf-8'))

        client_socket.close()
    except Exception as e:
        print(e)
        exit(0)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print(f"[SERVER STARTED] Listening on {HOST}:{PORT}")

clients = []

while True:
    try:
        client_socket, client_address = server.accept()
        clients.append(client_socket)

        client_handler = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_handler.start()

    except Exception as e:
        print(e)
        exit(0)