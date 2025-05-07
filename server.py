import socket, threading, pickle

HOST = "localhost"
PORT = 5000


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()
print(f"Servidor rodando na porta: {PORT}")


clients = []

def receive_data(conn, addr):
  clients.append(conn)
  print(f"Um novo cliente se conectou: {addr}")

  while True:
    data = pickle.loads(conn.recv(1024))
    print(data)
    
    for client in clients:
      if conn != client:
        client.sendall(pickle.dumps(data))


while True:
  conn, addr = server.accept()
  threading.Thread(target=receive_data, args=(conn, addr), daemon=True).start()

server.close()