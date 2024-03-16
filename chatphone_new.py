import socket
import threading


HOST = '192.168.1.141'  
PORT = 8000
class chatphoe:
    def __init__(self):
        self.port = PORT
        self.data = ''
    def recv_task(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(('0.0.0.0', self.port))
        self.server_socket.listen(1)
        client_socket, client_address = self.server_socket.accept()
        #print(f"Connection from {client_address[0]}:{client_address[1]}")
        self.connect_infor = f"Connection from {client_address[0]}:{client_address[1]}"
        self.ip = client_address[0]
        self.send('connected')
        while True:
            data = client_socket.recv(1024).decode('utf-8')
            if len(data)> 2:
                #print(f"Received data: {data}")
                self.data = data
        #client_socket.close()
    def check_connection(self):
        return self.connect_infor
    
    def get_message(self):
        if len(self.data)>0:
            output = self.data
            self.data = ''
            return output
        else:
            return False

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
            pass
            #print("It's not working!")