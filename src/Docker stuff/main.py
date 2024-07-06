import socket
import threading
from key_val_store import process_command


def handle_client(connfd):
    print("Connection accepted from client...")
    while True:
        data = connfd.recv(256)
        if not data:
            break
        command = data.decode().strip()
        process_command(command, connfd)
        if command == "QUIT":
            break
    connfd.close()


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 5678))
    server_socket.listen(5)
    print("Server started. Waiting for incoming connections...")

    while True:
        connfd, addr = server_socket.accept()
        client_thread = threading.Thread(target=handle_client, args=(connfd,))
        client_thread.start()


if __name__ == "__main__":
    main()
