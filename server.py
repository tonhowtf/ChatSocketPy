import socket
HOST = "localhost"
PORT = 5000
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()
print(f"Servidor rodando na porta: {PORT}")


clients = []

while True:
  conn, addr = server.accept()
  clients.append(conn)