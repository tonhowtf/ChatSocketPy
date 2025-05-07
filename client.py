import socket, pickle, threading

HOST = "localhost"
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST,PORT))
print("Cliente conectado ao servidor: ")

def receive_data():
  while True:
    data = pickle.loads(client.recv(1024))
    print(data)


threading.Thread(target=receive_data, daemon=True).start()


while True:
  msg = input("Digite sua mensagem: ")
  client.sendall(pickle.dumps(msg))