import socket
import threading

HOST = '0.0.0.0'
PORT = 12345

clients = []

def broadcast(message, sender_conn):
    for client in clients:
        if client != sender_conn:
            try:
                client.sendall(message)
            except:
                client.close()
                clients.remove(client)

def handle_client(conn, addr):
    print(f"Connected by {addr}")
    while True:
        try:
            data = conn.recv(1024)
            if not data:
                break
            broadcast(data, conn)
        except:
            break
    conn.close()
    clients.remove(conn)
    print(f"Disconnected {addr}")

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"Server listening on {HOST}:{PORT}")
    while True:
        conn, addr = server.accept()
        clients.append(conn)
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

if __name__ == "__main__":
    start_server()