import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.bind("127.0.0.1", 6379)

while True:
    message = input("Enter command (SET key val | GET key) or EXIT: ")
    client.send(message.encode("utf-8"))
    response = client.recv(1024).decode("utf-8")
    print(f"Server says: {response}")
