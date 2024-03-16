import socket
import threading


HOST = '172.20.10.6'  
PORT = 8000
class chatphoe:
    def __init__(self, ip = HOST,port = PORT):
        self.ip = ip
        self.port = port
    def recv_task(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(('0.0.0.0', self.port))
        self.server_socket.listen(1)
        client_socket, client_address = self.server_socket.accept()
        print(f"Connection from {client_address[0]}:{client_address[1]}")
        while True:
            data = client_socket.recv(1024).decode('utf-8')
            if len(data)> 2:
                print(f"Received data: {data}")
        client_socket.close()

    def recv_start(self):
        recv_thread = threading.Thread(target=self.recv_task)
        recv_thread.start()
    
    def send(self,message):
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((self.ip, self.port))
            client_socket.sendall(message.encode())
            client_socket.close()
        except:
            print("It's not working!")