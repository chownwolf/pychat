import socket
import threading

class ChatClient:
    def __init__(self, host='127.0.0.1', port=12345, on_message=None):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.on_message = on_message  # Callback for received messages
        self.running = False

    def connect(self):
        self.sock.connect((self.host, self.port))
        self.running = True
        threading.Thread(target=self.receive_messages, daemon=True).start()

    def send_message(self, message):
        self.sock.sendall(message.encode('utf-8'))

    def receive_messages(self):
        while self.running:
            try:
                data = self.sock.recv(1024)
                if data:
                    msg = data.decode('utf-8')
                    if self.on_message:
                        self.on_message(msg)
            except:
                break

    def close(self):
        self.running = False
        self.sock.close()