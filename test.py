import chatphone as cp

agent = cp.chatphoe('172.20.10.8')
agent.recv_start()

while True:
	agent.send(input('>'))
