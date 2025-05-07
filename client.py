import socket, pickle

HOST = "localhost"
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST,PORT))
print("Cliente conectado ao servidor: ")

while True:
  msg = input("Digite sua mensagem: ")
  client.sendall(pickle.dumps(msg))